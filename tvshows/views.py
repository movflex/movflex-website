from django.shortcuts import get_object_or_404 , render , redirect ,HttpResponseRedirect
from .models import Tvshow ,Category , Comment 
from accounts.models import UserProfile , Tvshow_Notification
import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from itertools import chain
from django.core.paginator import Paginator
from .filters import TvshowFilter
# Create your views here.

def tvshows(request):
    tv = Tvshow.objects.all().order_by('-publish_date')
    cat =  Category.objects.all()
    #filter 
    tvshowFilter = TvshowFilter(request.GET,queryset=tv)
    tv =tvshowFilter.qs

    #pagination
    paginator = Paginator(tv , 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'tvshows':page_obj,
        'tvshowFilter':tvshowFilter,
        'category': cat,
    }

    return render(request, 'tvshows/tvshows.html' , context)


    
def tvshow(request, tv_slug ):
    
    tv = Tvshow.objects.get(slug=tv_slug)
    
    
    like = Tvshow.objects.filter(category=tv.category , release_year=tv.release_year).exclude(name=tv.name).order_by('-imbd')

    part = Tvshow.objects.filter(name=tv.name).order_by('-season')

    director = tv.director.all()
    writer = tv.writer.all()
    show=list(chain(director , writer ))
    cast = tv.casts.all()

    com = Comment.objects.filter(tvshow_name=tv).exclude(user_nam=request.user.id)
    mycom = Comment.objects.filter(user_nam=request.user.id ,tvshow_name=tv)

    tag = tv.tags.all()

    favorits =True
    if request.user.is_authenticated:
        if UserProfile.objects.filter( user=request.user, tvshow_favorits=tv).exists():
            favorits =True
        else:
            favorits =False
    else:
        pass
    
    context = {
        'tv':tv,
        'casts':cast,
        'dirs_wrs':show,
        'comments':com,
        'mycomment':mycom,
        'tvshows':like,
        'parts':part,
        'tags':tag,
        'favorits':favorits

    }
    return render(request, 'tvshows/tvshow.html' , context )


def tvshow_add_comment(request ):
        #varibals
        
        date = datetime.datetime.now()
        user = request.GET['user']
        tvshow = request.GET['tvshow']
        evalute = request.GET['evalute']
        comment = request.GET['comment']
        
        if request.method == 'GET':
            userName = User.objects.get(username=user)
            tvshowName = Tvshow.objects.get(id=tvshow)
            if comment and evalute:
                comments = Comment(user_nam=userName , tvshow_name=tvshowName , comment=comment , evalute=evalute ,comment_date=date)
                comments.save()
                #Success Message 
                return redirect('/tvshows/tvshow/' + tvshowName.slug )
        

def tvshow_edit_comment(request):

        date = datetime.datetime.now()
        tvshow = request.GET['tvshow']
        evalute = request.GET['evalute']
        com = request.GET['comment']
        com_id = request.GET['com_id']
        
        if request.method == 'GET':
            
            tvshowName = Tvshow.objects.get(id=tvshow)
            editComment = Comment.objects.get(id=com_id)
            
            editComment.comment = com
            editComment.evalute = evalute
            editComment.comment_date = date
            editComment.save()
            
            return redirect('/tvshows/tvshow/' + tvshowName.slug )


def tvshow_del_comment(request , id , tv_id):
    com_del = get_object_or_404(Comment , id=id)

    if request.method == 'GET':
        com_del.delete()
        return redirect('/tvshows/tvshow/' +str(tv_id))

    return render(request, 'tvshows/tvshow.html')


#Favourits Functions 


def add_tvshow_favourits(request , tv_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        tv_fav = Tvshow.objects.get(pk=tv_id)
        if UserProfile.objects.filter( user=request.user, tvshow_favorits = tv_fav).exists():
            if request.LANGUAGE_CODE == 'en':
                messages.info(request, 'already exists in favorites')
            else:
                messages.info(request, 'موجود بالفعل بالمفضلة')
            
        else:
            userprofile =UserProfile.objects.get(user=request.user)
            userprofile.tvshow_favorits.add(tv_fav)
            if request.LANGUAGE_CODE == 'en':
                messages.success(request, 'added to favorites')
            else:
                messages.success(request, 'تم اضافة الى المفضلة')
            

    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/tvshows/tvshow/' + tv_fav.slug)


def del_tvshow_favourits(request, tv_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        tv_fav = Tvshow.objects.get(pk=tv_id)
        if UserProfile.objects.filter( user=request.user, tvshow_favorits = tv_fav).exists():
            userprofile =UserProfile.objects.get(user=request.user)
            userprofile.tvshow_favorits.remove(tv_fav)
            
        else:
            messages.error(request, 'not in  favorites')

    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/accounts/show_favourits')


# History functions


def add_tvshow_history(request , tv_id , url):
    if request.user.is_authenticated and not request.user.is_anonymous:
        tv_fav = Tvshow.objects.get(pk=tv_id)
        if UserProfile.objects.filter( user=request.user, tvshow_history= tv_fav).exists():
            return redirect("http://"+url)            
        else:
            userprofile =UserProfile.objects.get(user=request.user)
            userprofile.tvshow_history.add(tv_fav)
            return redirect("http://"+url)            

            
            

    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/tvshows/tvshow/' + tv_fav.slug )


def del_tvshow_history(request, tv_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        tv_fav = Tvshow.objects.get(pk=tv_id)
        if UserProfile.objects.filter( user=request.user, tvshow_history= tv_fav).exists():
            userprofile =UserProfile.objects.get(user=request.user)
            userprofile.tvshow_history.remove(tv_fav)
            
        

    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/accounts/show_history')


#Notifications 

def add_tvshow_notify(request, tv_id):
        
    if request.user.is_authenticated and not request.user.is_anonymous:
        user = User.objects.get(username=request.user)
        tvshow = Tvshow.objects.get(id=tv_id)
        if Tvshow_Notification.objects.filter(user=user , show=tvshow).exists():
            pass
        else:
            noti = Tvshow_Notification(user=user , show=tvshow)
            noti.save()
        if request.LANGUAGE_CODE == 'en':
            messages.success(request, 'you will be notify when its available')
        else:
            messages.success(request, 'سيتم اشعارك عندما يكون متاح')
        
    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/tvshows/tvshow/' + tvshow.slug )

def read_tvshow_notify(request ,id , tv_id ):
    user = User.objects.get(username=request.user)
    tvshow = Tvshow.objects.get(id=tv_id)
    if Tvshow_Notification.objects.filter(id=id).exists():
        noti = Tvshow_Notification.objects.get(id=id)
        if noti.read ==False:
            noti.read=True
            noti.save()
            return redirect('/tvshows/tvshow/' + tvshow.slug)
        else:
            return redirect('/tvshows/tvshow/' + tvshow.slug)
