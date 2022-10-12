from django.urls import path
from .consumers import WSConsumer, ChatConsumer, GraphConsumer

ws_urlpatterns=[
    path('ws/some_url/',WSConsumer.as_asgi()),
    path('ws/socket-server/',ChatConsumer.as_asgi()),
    path('ws/graph/',GraphConsumer.as_asgi()),
]