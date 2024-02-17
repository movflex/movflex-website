from django.shortcuts import render
from tvshows.models import Tvshow 
from movies.models import Movie
from channels.models import Channel
from pages.models import Release_year , Category 
from itertools import chain
from operator import attrgetter
from django.db.models import Q
# Create your views here.
def top(request):

    
    mov =  Movie.objects.all()
    Mcount = mov.count()
    tv = Tvshow.objects.all()
    Tvcount = tv.count()

    cat = Category.objects.all()

    chan = Channel.objects.all()

    t_mov = Movie.objects.filter(coming_soon=False).order_by('release_year','-imbd' , 'number_views')
    t_tv = Tvshow.objects.filter(coming_soon=False).order_by('release_year','-imbd' , 'number_views')
    top = sorted(chain(t_mov , t_tv ), key=lambda obj: obj.imbd , reverse=True)

    year = Release_year.objects.all().order_by('year')


    re = Release_year.objects.all()
    


    context={
        'Mcount':Mcount,
        'Tvcount':Tvcount,
        'channels':chan,
        'category':cat,
        'years':year,
        'release':re,
        'tops':top,
    }
    return render(request, 'pages/top.html' , context)

def Get_top(request):

    typee = request.GET['typee']
    release_year = request.GET['year']

    if typee == '1':
        top = Movie.objects.filter(release_year=release_year , coming_soon=False).order_by('-imbd', 'number_views')

    else:
        top = Tvshow.objects.filter(release_year=release_year , coming_soon=False).order_by('-imbd', 'number_views')
        
    mov =  Movie.objects.all()
    Mcount = mov.count()
    tv = Tvshow.objects.all()
    Tvcount = tv.count()

    cat = Category.objects.all()

    chan = Channel.objects.all()

    year = Release_year.objects.all().order_by('year')

    re = Release_year.objects.all()

    
    context={
        'Mcount':Mcount,
        'Tvcount':Tvcount,
        'channels':chan,
        'category':cat,
        'years':year,
        'release':re,
        'tops':top,
    }
    return render(request, 'pages/top.html' , context)

    