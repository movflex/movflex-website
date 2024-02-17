from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib import messages
from movies.models import Movie 
from tvshows.models import Tvshow 
from channels.models import Channel
from cast_and_crew.models import Cast,Director,Writer
from pages.models import Category,Language ,Release_year ,Tag
from accounts.models import UserProfile
from django.db.models import Q
from itertools import chain
from random import shuffle
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404 , render

# Create your views here.
# Show Home page content
def index(request):
    recommend = None
    if request.user.is_authenticated:
        userprofile = UserProfile.objects.get(user=request.user)
        cat = userprofile.favorit_category
        re_mov = Movie.objects.filter(category=cat)
        re_tv = Tvshow.objects.filter(category=cat)
        recommend =sorted(chain(re_mov , re_tv ) , key=lambda obj: obj.publish_date , reverse=True)

    tr_mov = Movie.objects.filter(is_trend=True)
    tr_tv = Tvshow.objects.filter(is_trend=True)
    trend =sorted(chain(tr_mov , tr_tv ) , key=lambda obj: obj.publish_date , reverse=True)

    so_mov =Movie.objects.filter(coming_soon=True)
    so_tv = Tvshow.objects.filter(coming_soon=True)
    soon = sorted(chain(so_mov , so_tv ) , key=lambda obj: obj.publish_date , reverse=True)
    
    new_mov = Movie.objects.all()
    new_tv = Tvshow.objects.all()
    new =sorted(chain(new_mov , new_tv ) , key=lambda obj: obj.publish_date , reverse=True)

    top_mov = Movie.objects.filter(imbd__gte=8.0,coming_soon=False)
    top_tv = Tvshow.objects.filter(imbd__gte=8.0,coming_soon=False)
    top =sorted(chain(top_mov , top_tv ) , key=lambda obj: obj.publish_date , reverse=True)
    

    context={
        'recommends':recommend,
        'trends':trend,
        'soons':soon,
        'news':new,
        'tops':top,
    }
    return render(request, 'pages/index.html' , context)

# User search and show results 
def search(request):
    mov = Movie.objects.all()
    tv = Tvshow.objects.all()
    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        mov = mov.filter(Q(name__icontains=name))
        tv = tv.filter(Q(name__icontains=name))
        search =sorted(chain(mov , tv ) , key=lambda obj: obj.publish_date , reverse=True)

        

    context={
        'search_result':search,
        'movies':mov,
        'tvshows':tv,
        'searchfiled':name
    }

    return render(request, 'pages/search.html' , context)

# Show list of movies that has the same tag
def movies_tag(request , tag_slug):

    tag = Tag.objects.get(slug=tag_slug)
    show = Movie.objects.filter(tags=tag)

    context={
        'shows':show,
        'tag_titel':tag.titel
        
    }

    return render(request, 'pages/tags.html' , context)

# Show list of tvshows that has the same tag
def tvshows_tag(request , tag_slug ):

    tag = Tag.objects.get(slug=tag_slug)
    show = Tvshow.objects.filter(tags=tag)

    context={
        'shows':show,
        'tag_titel':tag.titel
        
    }

    return render(request, 'pages/tags.html' , context)

# Show cast works 
def cast_detailes(request , cast_slug):

    cast = Cast.objects.get(slug=cast_slug)
    mov = Movie.objects.filter(casts=cast)
    mcount = mov.count()
    tv = Tvshow.objects.filter(casts=cast)
    tcount = tv.count()
    
    job_name = 'an Actor'
    job_name_ar = 'ممثـل'
    

    a_ll = sorted(chain(mov , tv ) , key=lambda obj: obj.publish_date , reverse=True)
    

    paginator = Paginator(a_ll , 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = {
        'show':cast,
        'all':page_obj,
        'job_name':job_name,
        'job_name_ar':job_name_ar,
        'mcount':mcount,
        'tcount':tcount,
    }
    return render(request, 'pages/show_detailes.html' , context)

# Show director works 
def director_detailes(request , dir_slug):

    director = Director.objects.get(slug=dir_slug)
    mov = Movie.objects.filter(director=director)
    mcount = mov.count()
    tv = Tvshow.objects.filter(director=director)
    tcount = tv.count()
    
    job_name = 'a Director'
    job_name_ar = 'مخرج'
    
    a_ll = sorted(chain(mov , tv ) , key=lambda obj: obj.publish_date , reverse=True)
    paginator = Paginator(a_ll , 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = {
        'show':director,
        'all':page_obj,
        'job_name':job_name,
        'job_name_ar':job_name_ar,
        'mcount':mcount,
        'tcount':tcount,
    }
    return render(request, 'pages/show_detailes.html' , context)

# Show writer works 
def writer_detailes(request , wr_slug):

    writer = Writer.objects.get(slug=wr_slug)
    mov = Movie.objects.filter(writer=writer)
    mcount = mov.count()
    tv = Tvshow.objects.filter(writer=writer)
    tcount = tv.count()
    
    job_name = 'a Writer'
    job_name_ar = 'كاتب'
    

    a_ll = sorted(chain(mov , tv ) , key=lambda obj: obj.publish_date , reverse=True)

    paginator = Paginator(a_ll , 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = {
        'show':writer,
        'all':page_obj,
        'job_name':job_name,
        'job_name_ar':job_name_ar,
        'mcount':mcount,
        'tcount':tcount,
    }
    return render(request, 'pages/show_detailes.html' , context)

# Error pages
def error_500(request):
    return render(request, 'error/500.html' , status=500)

def error_404(request , exception):
    return render(request, 'error/404.html' , status=404)
