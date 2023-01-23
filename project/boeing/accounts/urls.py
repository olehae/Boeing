"""
I created this file manually, it is used to define urlpatterns within the accounts/ path
"""

from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.sign_up_view, name="signup"),  # show builtin SignUpView in accounts/signup/ path
    path("emailconfirmation/", views.email_confirmation_view, name="emailconfirmation"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout")
]
