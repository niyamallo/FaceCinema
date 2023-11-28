from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


# token = Token.objects.create(user=...)

# Create your views here.
# @api_view(['POST'])
# def signup(request):
# 	#1-1. Client에서 온 데이터를 받아서
#     password = request.data.get('password')
#     password_confirmation = request.data.get('passwordConfirmation')
		
# 	#1-2. 패스워드 일치 여부 체크
#     if password != password_confirmation:
#         return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
# 	#2. UserSerializer를 통해 데이터 직렬화
#     serializer = UserSerializer(data=request.data)
    
# 	#3. validation 작업 진행.password 직렬화
#     if serializer.is_valid(raise_exception=True):
#         user = serializer.save()

#         user.set_password(request.data.get('password'))
#         user.save()
        
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
@api_view(['GET'])
def profile(request):
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def info(request):
    # print(request.data)
    users = request.data.get('users')
    movies = []
    ages = []
    for user in users:
        user = get_object_or_404(get_user_model(), pk=user)
        serializer = UserSerializer(user)
        age = serializer.data.get('age')
        like_movies = serializer.data.get('like_movies')

        for movie in like_movies:
            if movie not in movies:
                movies.append(movie)
            # 연령별 추천
            if age==user.age and movie not in ages:
                ages.append(movie)
    return Response([movies, ages])