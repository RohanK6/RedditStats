from django.shortcuts import render
from django.http import HttpResponse
from . import reddit

# Create your views here.

reddit = reddit.Reddit()

def index(request):
    return HttpResponse('<h1> Hello </h1>')