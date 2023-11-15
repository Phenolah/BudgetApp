from django.shortcuts import render, redirect
from .serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .forms import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.
@require_http_methods(["GET", "POST"])
def RegistrationView(request):
    form = UserRegistrationForm(request.POST)
    context = {}
    template_name = 'authentication/registration.html'

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            login(request,user)
            messages.sucess(request, f"Hey {username}, your account has been created")
            return redirect('home')
        else:
            form = UserRegistrationForm()
            context = {
                'form': form
            }
    return render(request, template_name , context)

@require_http_methods(["GET", "POST"])
def loginView(request):
    form = UserLoginForm(request.POST)
    context = {
        'form': form
    }
    # redirect authenticated user to homepage
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            # If user credentials are valid login in te user
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        return render(request, "authentication/registration.html", context)
