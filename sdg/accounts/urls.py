from django.urls import path

# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import 

from . import views

urlpatterns = [
    path('', views.home, name="accounts_home"),
    path('login', views.login, name="login"),
    path('register', views.signup, name="register"),
    path('logout', views.logout_view, name="logout_view")
]
