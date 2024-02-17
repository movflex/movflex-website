from django import template
from django.contrib.auth.models import User
from django.http import HttpResponse 
from accounts.models import Movie_Notification , Tvshow_Notification
from random import shuffle
register = template.Library()
@register.filter
def notifications(request):
    if request.user.is_authenticated:
        mov =Movie_Notification.objects.filter(user__username=request.user.username, show__coming_soon=False , read=False).count()
        tv = Tvshow_Notification.objects.filter(user__username=request.user.username, show__coming_soon=False , read=False).count()
        
        
        return mov+tv 

    else:
        pass