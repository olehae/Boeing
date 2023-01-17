from django.urls import path
from . import views
from django.http import HttpResponse

# URL Configuration
urlpatterns = [
    path("", views.overview, name="overview"),
    path("flight01", views.checkbox, name="flight01"),
    path("flight02", views.checkbox, name="flight02"),
    path("flight03", views.checkbox, name="flight03"),
]
