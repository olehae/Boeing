# I created this file manually, it is used to define urlpatterns within the booking/ path

from django.urls import path
from . import views
from boeing.helperfunctions import get_flights

urlpatterns = [
    path("", views.overview, name="overview")
]

for flight in get_flights().keys():
    urlpatterns.append(path(flight, views.checkbox, name=flight))
