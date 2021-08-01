from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils import timezone


# Create your models here.


class UserApiToken(models.Model):
    # ID would be created automatically
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    USER_API_TOKEN = models.CharField(max_length=100, default=None, null=True)
    IS_ACTIVE = models.BooleanField(blank=False, default=False, null=False)
    CREATED_DATE = models.DateTimeField(null=False, default=timezone.now)
    UPDATED_DATE = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.USER_API_TOKEN


class ImbdRatedMovies(models.Model):
    # ID would be created automatically
    POPULARITY = models.DecimalField(max_digits=5, decimal_places=1)
    DIRECTOR = models.CharField(max_length=254, default="HIDDEN", null=False)
    GENRE = ArrayField(models.CharField(max_length=50, blank=True, default=''), size=15, default=list)
    IMDB_SCORE = models.DecimalField(max_digits=5, decimal_places=1)
    MOVIE_NAME = models.CharField(max_length=254, default="", null=False)
    CREATE_USER = models.CharField(max_length=254, default="abc@admin.com", null=False)
    UPDATE_USER = models.CharField(max_length=254, default="abc@admin.com", null=True)
    CREATED_DATE = models.DateTimeField(null=False, default=timezone.now)
    UPDATED_DATE = models.DateTimeField(null=True)

    def __str__(self):
        return self.MOVIE_NAME
