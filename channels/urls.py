from django.urls import path 
from .  import views

urlpatterns = [
    path('' , views.channels , name='channels' ),
    path('<str:chan_slug>' , views.channel , name='channel' ),
    
]