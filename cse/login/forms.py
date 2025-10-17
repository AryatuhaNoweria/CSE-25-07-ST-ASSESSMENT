from django import forms 
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
from .models import User

class Sign_UpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['Full_Name','Email','Phone_Number','Password1','Password2']


class LoginForm (AuthenticationForm):
    Username = forms.CharField(max_length=255, label ="Email or Phone Number")
    Password = forms.CharField()


