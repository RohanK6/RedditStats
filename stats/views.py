from django.shortcuts import render
from . import reddit

# Create your views here.

reddit = reddit.Reddit()

def index(request):
    return render(request, 'stats/index.html')

def register(request):
    return render(request, 'stats/register.html')

def login(request):
    return render(request, 'stats/login.html')

def logout(request):
    return render(request, 'stats/logout.html')

def dashboard(request):
    return render(request, 'stats/dashboard.html')