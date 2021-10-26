from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from stats.models import Account
from django import forms

class AccountForm(UserCreationForm):
    email = forms.EmailField(max_length=255)
    reddit_username = forms.CharField(max_length=255)


    class Meta:
        model = Account
        fields = ('email', 'username', 'reddit_username', 'password1', 'password2')