from django.shortcuts import render, redirect
from .serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .forms import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
@require_http_methods(["GET", "POST"])
def RegistrationView(request):
    template_name = 'authentication/registration.html'

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
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
