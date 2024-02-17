from django.urls import path 
from .  import views

urlpatterns = [ 
    path('' , views.tvshows , name='tvshows' ),
    path('tvshow/<str:tv_slug>' , views.tvshow , name='tvshow' ),
    path('tvshow_add_comment/' , views.tvshow_add_comment , name='tvshow_add_comment' ),
    path('tvshow_edit_comment/' , views.tvshow_edit_comment , name='tvshow_edit_comment' ),
    path('tvshow_del_comment/<int:id>+<int:tv_id>' , views.tvshow_del_comment , name='tvshow_del_comment' ),
    #favourits
    path('add_tvshow_favourits/<int:tv_id>' , views.add_tvshow_favourits , name='add_tvshow_favourits' ),
    path('del_tvshow_favourits/<int:tv_id>' , views.del_tvshow_favourits , name='del_tvshow_favourits' ),

    #history
    path('add_tvshow_history/<int:tv_id>+<str:url>' , views.add_tvshow_history  , name='add_tvshow_history' ),
    path('del_tvshow_history/<int:tv_id>' , views.del_tvshow_history  , name='del_tvshow_history' ),
    #notification
    path('add_tvshow_notify/<int:tv_id>' , views.add_tvshow_notify , name='add_tvshow_notify' ),
    path('read_tvshow_notify/<int:id>+<int:tv_id>' , views.read_tvshow_notify , name='read_tvshow_notify' ),
    
]
