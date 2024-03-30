from django.urls import re_path

from mysite import consumers

websocket_urlpatterns = [
    re_path(r'ws/clock/', consumers.ClockConsumer.as_asgi()),
]