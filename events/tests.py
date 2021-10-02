import datetime
from unittest.mock import patch

import pytest
import http
from django.conf import settings
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.test import Client
from events.models import Event, UserProfile


# TestOK
def test_ok():
    assert 2+2 == 4


# TestFail
def test_fail():
    assert False


# HomePageView test
@pytest.mark.django_db
def test_index(client):
    response = client.get("")
    assert response.status_code == 200


# AllEventsView test
@pytest.mark.django_db
def test_events(client):
    response = client.get('/events/')
    assert response.status_code == 200


#TODO test nie przechodzi (slug?)
# SingleEvent test
@pytest.mark.django_db
def test_event_detail(client):
    response = client.get('/events/kreatywne-zabawy')
    assert response.status_code == 200


# LoginPage test
@pytest.mark.django_db
def test_login(client):
    response = client.get('/login/')
    assert response.status_code == 200
    user = User.objects.create_user(username="test_user", password="test_password")
    response = client.post("/login/",
        form={
            "username": "test_user",
            "password": "test_password",
        },
    )
    assert response.status_code == 200
    assert User.objects.count() == 1


# CreateUser test
@pytest.mark.django_db
def test_create_user(client):
    response = client.get('/create_user/')
    assert response.status_code == 200

