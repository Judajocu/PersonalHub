from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Users.models import CustomUser

class CustomUserCreation(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email', 'first_name', 'last_name', 'password', 'user_permissions')