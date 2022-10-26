# Чат

> Базовый чат на django, с использованием django-channels


## Redis

	$ docker run -p 6379:6379 -d redis:5


## Базовый Consumer/Producer

	>>> import channels.layers
	>>> channel_layer = channels.layers.get_channel_layer()
	>>>
	>>> from asgiref.sync import async_to_sync
	>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
	>>> async_to_sync(channel_layer.receive)('test_channel')
	{'type': 'hello'}

## TODO

* Unit-testing/Selenium testing
* Adding admin-only chat rooms.
* Sending the last ten messages to the user when they join a chat room.
* Allowing users to edit and delete messages.
* Adding '{user} is typing' functionality.
* Adding message reactions.
