from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import AccountForm
from stats.models import Account
from . import reddit
from django.contrib import messages

# Create your views here.

reddit = reddit.Reddit()

def index(request):
    return render(request, 'stats/index.html')

def register(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)

        if form.is_valid():
            form.save()
            
            email = form.cleaned_data['email']
            reddit_username = form.cleaned_data['reddit_username']
            unhashed_password = form.cleaned_data['password1']

            account = authenticate(email=email, password=unhashed_password)

            messages.success(request, f'Account created for {email}')

            return redirect('login')
            
        else:
            context = {'form': form}

    else:
        form = AccountForm()
        context = {'form': form}

    return render(request, 'stats/register.html', context)

def login(request):
    return render(request, 'stats/login.html')

@login_required
def logout(request):
    return render(request, 'stats/logout.html')

@login_required
def dashboard(request):
    print(request.user.reddit_username)
    return render(request, 'stats/dashboard.html')