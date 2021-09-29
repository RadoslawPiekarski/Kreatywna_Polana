from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main-page"),
    path("events/", views.events, name="all-events"),
    path("events/<slug:slug>", views.event_detail, name="single-event"),
    path("login/", views.login, name="login"),
    path("create-user/", views.create_user, name="create-user"),
]
