from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    release_date = models.DateField()
    adult = models.BooleanField()
    popularity = models.FloatField()
    # title = models.TextField()
    # original_title = models.TextField()
    # overview = models.TextField()
    # genres = models.ManyToManyField(Genre)
    # poster_path = models.TextField()
    # vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    # vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    # release_date = models.TextField()
    # adult = models.BooleanField()
    # # runtime = models.IntegerField(validators=[MinValueValidator(0)])
    # popularity = models.FloatField(validators=[MinValueValidator(0)])
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies')
    # wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')
    # watched_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watched_movies')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
