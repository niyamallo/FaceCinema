from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings
import requests
import json


from .models import Genre, Movie, Review
from .serializers import ReviewSerializer, ReviewListSerializer, MovieListSerializer, MovieSerializer

from random import sample

# API KEY 설정
api_key = "89a670d3011bed58f83c7337920d53ff"

# 언어 설정
language = "ko-KR"

# API 호출을 위한 URL 설정
# 장르
genres_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language={language}"

# API 호출 및 응답 데이터 가져오기
genres_response = requests.get(genres_url)
genres_data = genres_response.json()

# 장르 목록 추출
genres = genres_data["genres"]

# JSON 파일로 저장(장르)
with open("movies/fixtures/genres.json", "w", encoding="utf-8") as f:
    json.dump(genres, f, indent=4, ensure_ascii=False)

# 1주일간의 인기영화 목록(60개)
movies = []
for page in range(1,4):
    movies_url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}&language={language}&page={page}"
    movies_response = requests.get(movies_url)
    movies_data = movies_response.json()

    # 영화 목록 추출
    movies += movies_data["results"]

# JSON 파일로 저장(영화목록)
with open("movies/fixtures/movies.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, indent=4, ensure_ascii=False)
    
# Create your views here.
@api_view(['GET'])
def make_database(request):
    with open("movies/fixtures/genres.json", "r", encoding="utf-8") as f:
        genres_data = json.load(f)
    for genre_data in genres_data:
        name = genre_data["name"]
        # 중복된 데이터 확인
        genre, created = Genre.objects.get_or_create(name=name)

        if created:
            # 새로운 데이터인 경우에만 생성
            genre.save()
    
    with open("movies/fixtures/movies.json", "r", encoding="utf-8") as f:
        movies_data = json.load(f)

    for movie_data in movies_data:
        # 필요한 필드 추출
        valid_data = {
            'title': movie_data.get('title', ''),
            'original_title': movie_data.get('original_title', ''),
            'overview': movie_data.get('overview', ''),
            'poster_path': movie_data.get('poster_path', ''),
            'backdrop_path': movie_data.get('backdrop_path', ''),
            'vote_average': movie_data.get('vote_average', 0),
            'vote_count': movie_data.get('vote_count', 0),
            'release_date': movie_data.get('release_date', ''),
            'adult': movie_data.get('adult', False),
            'popularity': movie_data.get('popularity', 0.0),
        }

        # 중복된 데이터 확인
        title = valid_data['title']
        existing_movie = Movie.objects.filter(title=title).first()
        if existing_movie:
            continue  # 이미 존재하는 데이터면 건너뛰기

        # Movie 객체 생성
        movie = Movie(**valid_data)
        movie.save()

    return Response({"message": "Database updated"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def movies(request):
    # with open("movies/fixtures/movies.json", "r", encoding="utf-8") as f:
    #     movies_data = json.load(f)

    # for movie_data in movies_data:
    #     valid_data = {}

    #     # 필요한 필드만 추출
    #     valid_fields = ["title", "genres", "release_date"]

    #     for field in valid_fields:
    #         if field in movie_data:
    #             valid_data[field] = movie_data[field]
    #         else:
    #             valid_data[field] = None

    #     # Movie 객체 생성
    #     movie = Movie.objects.create(**valid_data)
        
    #     # genres 필드 처리
    #     if "genre" in movie_data:
    #         genres_data = movie_data["genre"]
    #         genres = []

    #         for genre_name in genres_data:
    #             genre, _ = Genre.objects.get_or_create(name=genre_name)
    #             genres.append(genre)

    #         movie.genres.set(genres)
        
    # movie_list = get_object_or_404(Movie)
    movie_list = get_list_or_404(Movie)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def reviews(request, movie_pk):
    if request.method == 'GET':
        review_list = Review.objects.all().filter(movie_id=movie_pk)
        serializer = ReviewListSerializer(review_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie = get_object_or_404(Movie, pk=request.data.get('movie'))

            pre_point = movie.vote_average * movie.vote_count

            point = pre_point + int(request.data.get('rank'))
            count = movie.vote_count + 1
            new_vote_average = round(point / count, 2)

            movie.vote_average = new_vote_average
            movie.vote_count = count
            movie.save()

            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_review(request, my_pk):
    if request.method == 'GET':
        review_list = Review.objects.all().filter(user_id=my_pk)
        serializer = ReviewListSerializer(review_list, many=True)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)

        if serializer.is_valid(raise_exception=True):
            movie = get_object_or_404(Movie, pk=request.data.get('movie'))
            pre_point = movie.vote_average * (movie.vote_count - 1)
            point = pre_point + int(request.data.get('rank'))
            count = movie.vote_count
            new_vote_average = round(point / count, 2)
            movie.vote_average = new_vote_average
            movie.vote_count = count
            movie.save()
            serializer.save(user=request.user)
            return Response(serializer.data)
        
        else:
            review = get_object_or_404(Review, pk=review_pk)
            movie = get_object_or_404(Movie, pk=review.movie_id)
            pre_point = movie.vote_average * (movie.vote_count)
            point = pre_point - review.rank
            count = movie.vote_count - 1
            new_vote_average = round(point / count, 2)
            movie.vote_average = new_vote_average
            movie.vote_count = count
            movie.save()
            review.delete()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def recommend(request):
    me_like = request.data.get('me_like')

    # 인기순
    favorite_movies = Movie.objects.all().order_by('-vote_average')[:10]
    favorite_serialize = MovieSerializer(favorite_movies, many=True)
    # 리뷰 기반 장르기반 추천
    user_movies_review = []
    # 배우기반 추천
    user_movies_actor = []
    # 감독기반 추천
    user_movies_director = []
    # 개봉년도
    # 제작 국가
    # 리뷰 기반 장르별
    reviews = Review.objects.all()
    for review in reviews:
        movie = Movie.objects.get(pk=review.movie_id)
        if not movie in user_movies_review:
            user_movies_review.append(movie)

    # 좋아요 기반추천
    my_user_like_movies = []
    user_like_movies = []
    # 좋아요 기반 추천
    like_movies = request.data.get('like_movies')
    for like_movie in like_movies:
        movie = get_object_or_404(Movie, pk=like_movie)
        if not movie in my_user_like_movies:
            my_user_like_movies.append(movie)
    # 내가 좋아요 한 것 제거
    for like_movie in my_user_like_movies:
        
        if like_movie.id not in me_like:
            user_like_movies.append(like_movie)
    
            
    
    # user_genre_serialize = MovieSerializer(user_movies_review, many=True)
    user_like_serialize = MovieSerializer(user_like_movies, many=True)
    
    # 연령대
    user_movies_age = []
    # 연령별 기반 추천
    me_age = request.data.get('me_age')
    for age in me_age:
        movie = get_object_or_404(Movie, pk=age)
        if not movie in user_movies_age:
            user_movies_age.append(movie)

    user_movies_age_serializer = MovieSerializer(user_movies_age, many=True)
    return Response([favorite_serialize.data, user_like_serialize.data, user_movies_age_serializer.data])

@api_view(['POST'])
def my_movie_like(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)


@api_view(['POST'])
def my_movie_dislike(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)
    

@api_view(['POST'])
def my_movie_wish(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)


@api_view(['POST'])
def movie_like(request, my_pk, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if me.like_movies.filter(pk=movie.pk).exists():
        me.like_movies.remove(movie.pk)
        liking = False
      
    else:
        me.like_movies.add(movie.pk)
        liking = True
  
    return Response(liking)


@api_view(['POST'])
def movie_dislike(request, my_pk, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if me.dislike_movies.filter(pk=movie.pk).exists():
        me.dislike_movies.remove(movie.pk)
        disliking = False
      
    else:
        me.dislike_movies.add(movie.pk)
        disliking = True
  
    return Response(disliking)


@api_view(['POST'])
def movie_wish(request, my_pk, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if me.wish_movies.filter(pk=movie.pk).exists():
        me.wish_movies.remove(movie.pk)
        wishing = False
      
    else:
        me.wish_movies.add(movie.pk)
        wishing = True
  
    return Response(wishing)


@api_view(['POST'])
def like_movie_users(request, my_pk):
    
    users = []
    movies = request.data.get('movies')

    for movie in movies:
        movie = get_object_or_404(Movie, pk=movie)
        serializer = MovieSerializer(movie)

    for user in serializer.data.get('like_users'):
        if user not in users:
            users.append(user)
    
    return Response(users)


@api_view(['POST'])
def dislike_movie_users(request, my_pk):
    
    users = []
    movies = request.data.get('movies')

    for movie in movies:
        movie = get_object_or_404(Movie, pk=movie)
        serializer = MovieSerializer(movie)

    for user in serializer.data.get('dislike_users'):
        if user not in users:
            users.append(user)
    
    return Response(users)


@api_view(['POST'])
def wish_movie_users(request, my_pk):
  
    users = []
    movies = request.data.get('movies')

    for movie in movies:
        movie = get_object_or_404(Movie, pk=movie)
        serializer = MovieSerializer(movie)

    for user in serializer.data.get('wish_users'):
        if user not in users:
            users.append(user)
    
    return Response(users)

@api_view(['GET'])
def recommend(request, month_pk):
    # 사용자로부터 입력받은 월 정보 (예: 3)
    month = month_pk
    # 해당 월의 영화 목록을 필터링
    movies = Movie.objects.filter(release_date__month=month)
    # 랜덤하게 3개의 영화 선택
    if len(list(movies)) >= 3:
        random_movies = sample(list(movies), 3)
    else:
        random_movies = list(movies)
    # 직렬화된 형식으로 응답
    serializer = MovieSerializer(random_movies, many=True)
    return Response(serializer.data)