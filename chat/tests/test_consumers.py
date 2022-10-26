import pytest
from channels.testing import (  # noqa flake8:skip
    ApplicationCommunicator,
    WebsocketCommunicator,
)
from django.test import TestCase

from ..consumers import ChatConsumer


@pytest.mark.asyncio
class TestChatConsumer(TestCase):
    async def test_chat_consumer_ws(self):
        communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "GET", "/chat/")
        connected, subprotocol = await communicator.connect()
        assert connected

    # async def test_app(self):
    #     communicator = ApplicationCommunicator(
    #         ChatConsumer.as_asgi(),
    #         {'type': 'http', 'message': 'test'})
    #     await communicator.send_input({
    #         "type": "http.request",
    #         "body": b"chunk one \x01 chunk two",
    #     })
    #     event = await communicator.receive_output(timeout=1)
