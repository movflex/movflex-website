from django.shortcuts import get_object_or_404 , render , redirect ,HttpResponseRedirect
from .models import Movie ,Category , Comment 
from django.contrib.auth.models import User
from accounts.models import UserProfile , Movie_Notification 
import datetime
from django.contrib import messages
from cast_and_crew.models import Cast ,Director ,Writer
from itertools import chain
from django.core.paginator import Paginator
from .filters import MovieFilter

# Create your views here.
# Show list of Moives
def movies(request):
    mov = Movie.objects.all().order_by('-publish_date')
    cat =  Category.objects.all()
    
    #filter
    movieFilter = MovieFilter(request.GET,queryset=mov)
    mov =movieFilter.qs

    #paginator
    paginator = Paginator(mov , 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'movies':page_obj,
        'movieFilter':movieFilter,
        'category': cat,
    }

    return render(request, 'movies/movies.html' , context)


# show content of each movie 
def movie(request, mov_slug ):

    mov = Movie.objects.get(slug=mov_slug)

    # to get similar movies
    like = Movie.objects.filter(category=mov.category , release_year=mov.release_year).exclude(name=mov.name).order_by('-imbd')
    # to show other parts of the movie
    part = Movie.objects.filter(name=mov.name).order_by('-season')

    # to show cast and crew
    director = mov.director.all()
    writer = mov.writer.all()
    show=list(chain(director , writer ))
    cast = mov.casts.all()

    # to show cooments 
    com = Comment.objects.filter(movie_name=mov).exclude(user_nam=request.user.id)
    mycom = Comment.objects.filter(user_nam=request.user.id ,movie_name=mov)

    # to show tags
    tag = mov.tags.all()
    
    # to check if the movie in user favourits list or not
    favorits =True
    if request.user.is_authenticated:
        if UserProfile.objects.filter( user=request.user, movie_favorits = mov).exists():
            favorits =True
        else:
            favorits =False
    else:
        pass

    context = {
        'mov':mov,
        'casts':cast,
        'dirs_wrs':show,
        'comments':com,
        'mycomment':mycom,
        'movies':like,
        'parts':part,
        'tags':tag,
        'favorits':favorits

    }
    return render(request, 'movies/movie.html' , context )

# User add comment
def mvoie_add_comment(request ):
       
    date = datetime.datetime.now()
    user = request.GET['user']
    movie = request.GET['movie']
    evalute = request.GET['evalute']
    comment = request.GET['comment']
    
    if request.method == 'GET':
        userName = User.objects.get(username=user)
        movieName = Movie.objects.get(id=movie)
        if comment and evalute:
            comments = Comment(user_nam=userName , movie_name=movieName , comment=comment , evalute=evalute ,comment_date=date)
            comments.save()
            return redirect('/movies/movie/' + movieName.slug )
        
        
        
        
# User edit comment
def movie_edit_comment(request):
    
    date = datetime.datetime.now()
    movie = request.GET['movie']
    evalute = request.GET['evalute']
    com = request.GET['comment']
    com_id = request.GET['com_id']
    
    if request.method == 'GET':
        
        movieName = Movie.objects.get(id=movie)
        editComment = Comment.objects.get(id=com_id)
        
        editComment.comment = com
        editComment.evalute = evalute
        editComment.comment_date = date
        editComment.save()
        #Success Message 
        
        return redirect('/movies/movie/' + movieName.slug )


# User delete comment
def movie_del_comment(request , id , mov_slug):
    com_del = get_object_or_404(Comment , id=id)

    if request.method == 'GET':
        com_del.delete()
        return redirect('/movies/movie/' +str(mov_slug))

    return render(request, 'movies/movie.html')

#Favourits Functions 
# User add to favourits list 
def add_movie_favourits(request , mov_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        mov_fav = Movie.objects.get(pk=mov_id)
        if UserProfile.objects.filter( user=request.user, movie_favorits = mov_fav).exists():
            if request.LANGUAGE_CODE == 'en':
                messages.info(request, 'already exists in favorites')
            else:
                messages.info(request, 'موجود بالفعل بالمفضلة')
            
        else:
            userprofile =UserProfile.objects.get(user=request.user)
            userprofile.movie_favorits.add(mov_fav)
            if request.LANGUAGE_CODE == 'en':
                messages.success(request, 'added to favorites')
            else:
                messages.success(request, 'تم اضافة الى المفضلة')
            

    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/movies/movie/' + mov_fav.slug)

# User remove from favourits list 
def del_movie_favourits(request, mov_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        mov_fav = Movie.objects.get(pk=mov_id)
        if UserProfile.objects.filter( user=request.user, movie_favorits = mov_fav).exists():
            userprofile =UserProfile.objects.get(user=request.user)
            userprofile.movie_favorits.remove(mov_fav)
           
        else:
            messages.error(request, 'not in  favorites')

    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/accounts/show_favourits')


# History functions
# Add to hitory automatic if user watch
def add_movie_history(request , mov_id , url):
    if request.user.is_authenticated and not request.user.is_anonymous:
        mov_fav = Movie.objects.get(pk=mov_id)
        if UserProfile.objects.filter( user=request.user, movie_history= mov_fav).exists():
            return redirect("http://"+url)            
        else:
            userprofile =UserProfile.objects.get(user=request.user)
            userprofile.movie_history.add(mov_fav)
            return redirect("http://"+url)            
            

    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/movies/movie/' + mov_fav.slug )

# User delete from history
def del_movie_history(request, mov_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        mov_fav = Movie.objects.get(pk=mov_id)
        if UserProfile.objects.filter( user=request.user, movie_history= mov_fav).exists():
            userprofile =UserProfile.objects.get(user=request.user)
            userprofile.movie_history.remove(mov_fav)
    
    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/accounts/show_history')

#Notifications 
# User request to be notified when is available
def add_movie_notify(request, mov_id):
        
    if request.user.is_authenticated and not request.user.is_anonymous:
        user = User.objects.get(username=request.user)
        movie = Movie.objects.get(id=mov_id)
        if Movie_Notification.objects.filter(user=user , show=movie).exists():
            pass
        else:
            noti = Movie_Notification(user=user , show=movie)
            noti.save()
        if request.LANGUAGE_CODE == 'en':
            messages.success(request, 'you will be notify when its available')
        else:
            messages.success(request, 'سيتم اشعارك عندما يكون متاح')
        
    else:
        messages.error(request, 'you must be logged in ')
    return redirect('/movies/movie/' + movie.slug)

# User read the notification
def read_movie_notify(request ,id , mov_id ):
    user = User.objects.get(username=request.user)
    movie = Movie.objects.get(id=mov_id)
    if Movie_Notification.objects.filter(id=id).exists():
        noti = Movie_Notification.objects.get(id=id)
        if noti.read ==False:
            noti.read=True
            noti.save()
            return redirect('/movies/movie/' + movie.slug)
        else:
            return redirect('/movies/movie/' + movie.slug)




