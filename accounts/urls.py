from django.urls import path 
from .  import views

urlpatterns = [
    path('login' , views.login , name='login' ),
    path('signup' , views.signup , name='signup' ),
    path('logout' , views.logout , name='logout' ),
    path('profile' , views.profile , name='profile' ),
    path('change_photo' , views.change_photo , name='change_photo' ),
    
    #password
    path('change_password' , views.change_password , name='change_password' ),
    path('forgot_password' , views.forgot_password , name='forgot_password' ),
    path('forgot_password/answer_question' , views.answer_question , name='answer_question' ),
    path('forgot_password/reseet_password' , views.reseet_password , name='reseet_password' ),
    #favourits
    path('show_favourits' , views.show_favourits , name='show_favourits' ),

    #history
    path('show_history' , views.show_history , name='show_history' ),
    path('clear_history' , views.clear_history , name='clear_history' ),

    #notifications
    path('show_notifications' , views.show_notifications , name='show_notifications' ),
    path('clear_notifications' , views.clear_notifications , name='clear_notifications' ),
]
