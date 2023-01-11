from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    path("", views.overview, name="overview"),
    path("test", views.checkbox, name="checkbox"),
]
