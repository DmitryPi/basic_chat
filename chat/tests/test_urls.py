import pytest
from django.urls import resolve, reverse

from ..models import Room


def test_index_url():
    assert "/chat/" == reverse("chat-index")
    assert "chat-index" == resolve("/chat/").view_name


@pytest.mark.django_db
def test_room_url():
    obj, created = Room.objects.get_or_create(name="test")
    assert "/chat/test/" == reverse("chat-room", kwargs={"room_name": obj.name})
    assert "chat-room" == resolve("/chat/test/").view_name
