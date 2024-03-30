from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application
from django.urls import path


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django.settings')


from .consumers import ClockConsumer


django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter([ # прописываем путь, по которому будет доступен Consumer, аналог urls
            path('ws', ClockConsumer.as_asgi())
        ])
    )
})