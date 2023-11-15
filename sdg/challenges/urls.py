from django.urls import path

# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import 

from . import views

urlpatterns = [
    path('', views.home, name="challenges_home"),
    path('create_challenge', views.home, name="challenge_create"),
]
