from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main-page"),
    path("events/", views.events, name="all-events"),
    path("events/<slug:slug>", views.event, name="single-event"),
]

