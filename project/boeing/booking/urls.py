from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    path("test", views.index, name="index"),
]
