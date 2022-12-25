"""
I created this file manually, it is used to define urlpatterns within the accounts/ path
"""

from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),  # show builtin SignUpView in accounts/signup/ path
]
