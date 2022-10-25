from django.contrib import admin  # noqa flake8:skip

from chat.models import Message, Room

admin.site.register(Room)
admin.site.register(Message)
