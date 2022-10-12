from django.urls import path
from .views import index, lobby, graph

urlpatterns = [
    path('',index,name='index'),
    path('lobby/',lobby,name='lobby'),
    path('graph/',graph,name='graph')
]
 