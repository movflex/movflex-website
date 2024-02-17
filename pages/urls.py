from django.urls import path 
from . import views 

urlpatterns = [
    path('' , views.index , name='index'),
    path('search/' , views.search , name='search' ),
    path('movies_tag/<str:tag_slug>' , views.movies_tag , name='movies_tag' ),
    path('tvshows_tag/<str:tag_slug>' , views.tvshows_tag , name='tvshows_tag' ),
    path('cast_detailes/<str:cast_slug>' , views.cast_detailes , name='cast_detailes' ),
    path('director_detailes/<str:dir_slug>' , views.director_detailes , name='director_detailes' ),
    path('writer_detailes/<str:wr_slug>' , views.writer_detailes , name='writer_detailes' ),
]
