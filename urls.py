"""IMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from my_App import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('get_social_details/', views.get_signup_data, name='get_details'),
    path('get_started/', views.get_started, name='get_started'),
    path('api/', views.user_api, name='user_api'),
    path('generate/', views.user_api, name='get_credentials'),
    path('setAdmin/', views.set_admin, name='set_Admin'),
    path('addData/', views.ManipulateData.as_view(), name="add_data"),
    path('updateData/<int:id>/', views.ManipulateData.as_view(), name="update_data"),
    path('deleteData/<int:id>/', views.ManipulateData.as_view(), name="delete_data"),
    path('getMovies/', views.get_movies, name="get_movies"),
    path('searchMovies/<str:movie>/', views.search_movies, name="search_movies"),
    path('logout/', views.user_logout, name='user_logout'),
]
