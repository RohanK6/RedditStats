from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usearch/', views.usearch, name='usearch'),
    path('usearch/<str:query>/', views.usearch_query, name='usearch_query'),
]
