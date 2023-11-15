from django.urls import path

# from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="goals_home"),
    path('create_goal', views.create_goal, name="goal_create"),
]
