from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import AccountForm, AccountAuthenticationForm
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

def account_login(request):
    context = {}

    user = request.user
    
    if user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')
    else:
        form = AccountAuthenticationForm()

    context['form'] = form

    return render(request, 'stats/login.html', context)

@login_required
def account_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('index')

@login_required
def dashboard(request):
    context = reddit.user_overview(request.user.reddit_username)
    return render(request, 'stats/dashboard.html', context)