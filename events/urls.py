from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main-page"),
    path("events/", views.Events.as_view(), name="all-events"),
    path("events/<slug:slug>", views.event_detail, name="single-event"),
    path("login/", views.Login.as_view(), name="login"),
    path("create-user/", views.CreateUser.as_view(), name="create-user"),
    path("parents_info/", views.parents_info_page, name="parents-info"),
    path("events/add_event", views.Events.as_view(), name="add-event")
]
