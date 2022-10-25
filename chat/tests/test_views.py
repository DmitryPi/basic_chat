import pytest
from django.test import Client
from django.urls import reverse

from ..models import Room


@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse("chat-index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_room_view():
    obj, created = Room.objects.get_or_create(name="test")
    client = Client()
    response = client.get(reverse("chat-room", kwargs={"room_name": obj.name}))
    assert response.status_code == 200
