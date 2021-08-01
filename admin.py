from django.contrib import admin
from my_App.models import UserApiToken, User, ImbdRatedMovies

# Register your models here.
admin.site.register(UserApiToken)
admin.site.register(ImbdRatedMovies)
