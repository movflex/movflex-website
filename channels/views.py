from django.shortcuts import get_object_or_404 , render
from .models import Channel
from movies.models import Movie
from tvshows.models import Tvshow
from itertools import chain
from django.core.paginator import Paginator
from random import shuffle
# Create your views here.

# Show list of channels
def channels(request):
    chan = Channel.objects.all()
    context ={
        'channels':chan
    }
    return render(request, 'channels/channels.html' , context)

# Show the content of each channel 
def channel(request , chan_slug):

    channel = Channel.objects.get(slug=chan_slug)
    mov = Movie.objects.filter(channel=channel)
    mcount = mov.count()
    tv = Tvshow.objects.filter(channel=channel)
    tcount = tv.count()
    
    show =sorted(chain(mov , tv ) , key=lambda obj: obj.publish_date , reverse=True)

    a_ll = sorted(chain(mov , tv ) , key=lambda obj: obj.publish_date , reverse=True)

    paginator = Paginator(a_ll , 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = {
        'chan':channel,
        'all':page_obj,
        'shows':show,
        'mcount':mcount,
        'tcount':tcount,
    }
    return render(request, 'channels/channel.html' , context)
