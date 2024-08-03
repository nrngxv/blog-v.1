#form for user registration
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # adding additional email form, it doesn't come pre included

    class Meta:
        model = User #this is a model that is saved in the database
        fields = ['username','email','password1','password2']