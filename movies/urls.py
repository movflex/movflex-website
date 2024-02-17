from django.urls import path 
from .  import views

urlpatterns = [
    path('' , views.movies , name='movies' ),
    path('movie/<str:mov_slug>' , views.movie , name='movie' ),
    path('movie_add_comment/' , views.mvoie_add_comment , name='mvoie_add_comment' ),
    path('movie_edit_comment/' , views.movie_edit_comment , name='movie_edit_comment' ),
    path('movie_del_comment/<int:id>+<str:mov_slug>' , views.movie_del_comment , name='movie_del_comment' ),
    #favourits
    path('add_movie_favourits/<int:mov_id>' , views.add_movie_favourits , name='add_movie_favourits' ),
    path('del_movie_favourits/<int:mov_id>' , views.del_movie_favourits , name='del_movie_favourits' ),
    #history
    path('add_movie_history/<int:mov_id>+<str:url>' , views.add_movie_history , name='add_movie_history' ),
    path('del_movie_history/<int:mov_id>' , views.del_movie_history  , name='del_movie_history' ),
    #notification
    path('add_movie_notify/<int:mov_id>' , views.add_movie_notify , name='add_movie_notify' ),
    path('read_movie_notify/<int:id>+<int:mov_id>' , views.read_movie_notify , name='read_movie_notify' ),

    
]
