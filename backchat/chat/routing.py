from django.urls import path

from chat import consumers

websocket_urlpatterns = [
    path('templates/<str:room_slug>/', consumers.ChatConsumer.as_asgi()),
]
