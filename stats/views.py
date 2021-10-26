from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm
from . import reddit

# Create your views here.

reddit = reddit.Reddit()

def index(request):
    return render(request, 'stats/index.html')

def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']

            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    else:
        form = ProfileForm()
        context = {'form': form}

    return render(request, 'stats/register.html', context)

def login(request):
    return render(request, 'stats/login.html')

@login_required
def logout(request):
    return render(request, 'stats/logout.html')

@login_required
def dashboard(request):
    return render(request, 'stats/dashboard.html')