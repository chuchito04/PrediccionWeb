from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.signout, name="logout"),
    path("formulario/", views.formulario, name="formulario"),
    path("resultado/", views.predict, name="resultado")
    
]
