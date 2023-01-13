"""
I created this file manually, it is used to define urlpatterns within the accounts/ path
"""

from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),  # show builtin SignUpView in accounts/signup/ path
    path("emailconfirmation/", views.EmailConfirmationView, name="emailconfirmation"),
    path("login/", views.LoginView, name="login"),
    path("logout/", views.LogoutView, name="logout")
]
