from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
# from models import User

def index(request):
    return render(request, 'user_dashboard/index.html')

def login(request):
    return render(request, 'user_dashboard/login.html')

def register(request):
    return render(request, 'user_dashboard/register.html')

def edit(request):
    return render(request, 'user_dashboard/edit.html')

def dashboard(request):
    return render(request, 'user_dashboard/dashboard.html')
