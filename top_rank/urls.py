from django.urls import path 
from .  import views

urlpatterns = [
    path('' , views.top , name='top' ),
    path('Get_top' , views.Get_top , name='Get_top' )

]