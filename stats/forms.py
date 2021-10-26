from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from stats.models import Account
from django import forms

class AccountForm(UserCreationForm):
    email = forms.EmailField(max_length=255)
    reddit_username = forms.CharField(max_length=255)


    class Meta:
        model = Account
        fields = ('email', 'username', 'reddit_username', 'password1', 'password2')

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")