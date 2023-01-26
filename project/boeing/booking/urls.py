# I created this file manually, it is used to define urlpatterns within the booking/ path

from django.urls import path
from . import views

urlpatterns = [
    path("", views.overview, name="overview"),
    path("flight01", views.checkbox, name="flight01"),
    path("flight02", views.checkbox, name="flight02"),
    path("flight03", views.checkbox, name="flight03"),
    path("flight04", views.checkbox, name="flight04"),
]
