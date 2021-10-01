import datetime
from unittest.mock import patch

import pytest
import http
from django.conf import settings
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.test import Client


# HomePageView
def test_index(client):
    response = client.get("")
    assert response.status_code == 200


# AllEventsView
def test_events(client):
    response = client.get('/events/')
    assert response.status_code == 200
