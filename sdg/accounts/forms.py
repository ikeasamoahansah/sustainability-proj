from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
# from .models import Post, UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["email", "username", "password1", "password2", "is_company"]