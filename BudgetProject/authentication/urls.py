from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegistrationView, name="register"),
    path('login', views.loginView, name="login"),

]