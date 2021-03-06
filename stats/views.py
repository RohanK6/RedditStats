from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.contrib import messages
from .forms import AccountForm, AccountAuthenticationForm
from .models import Account
from . import reddit

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

def usearch(request):
    if request.GET.get('redditor') != None:
        query = request.GET.get('redditor')
        return redirect('usearch_query', query)

    return render(request, 'stats/usearch.html')

def usearch_query(request, query):
    context = reddit.user_overview(query)

    if context == None:
        messages.error(request, f'{query} is not a valid Reddit user. Please check and try again.')
        return redirect('usearch')
        
    return render(request, 'stats/usearch_query.html', context)

def ssearch(request):
    if request.GET.get('subreddit') != None:
        query = request.GET.get('subreddit')
        return redirect('ssearch_query', query)

    return render(request, 'stats/ssearch.html')

def ssearch_query(request, query):
    context = reddit.subreddit_overview(query)

    if context == None:
        messages.error(request, f'{query} is not a valid subreddit. Please check and try again.')
        return redirect('ssearch')
        
    return render(request, 'stats/ssearch_query.html', context)

def leaderboard(request):
    popularSubreddits = reddit.popular_subreddits()

    counter = 1

    context = {}

    for subreddit in popularSubreddits:
        context[counter] = subreddit
        counter += 1

    return render(request, 'stats/leaderboard.html', {'context': context})