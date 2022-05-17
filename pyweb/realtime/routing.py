from django.urls import path
from .consumers import WSConsumer

websocket_urlpatterns = [
    path('ws/variable/', WSConsumer.as_asgi())
]