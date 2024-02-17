from django.shortcuts import render , redirect ,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth 
from itertools import chain
from .models import UserProfile , Movie_Notification , Tvshow_Notification
from channels.models import Channel
from movies.models import Movie
from tvshows.models import Tvshow
from pages.models import Category , Sequrty_question
import re
from random import shuffle
from django.core.files.storage import FileSystemStorage

# Create your views here.
# Login view
def login(request):

    if request.method == 'POST':

        username = request.POST['user']
        password = request.POST['pass']

        user = auth.authenticate(username=username , password=password)
        if user is not None:
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request, user)
            next_page = request.POST.get('next_page' , '/')
            return HttpResponseRedirect(next_page)
        else:
            if request.LANGUAGE_CODE == 'en':
                messages.error(request, 'invalid username or password !') 
            else:
                messages.error(request, ' !اسم مستخدم او كلمة مرور غير صحيحة') 

        return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')

# Logout view
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')

# singup view
def signup(request):
    cat = Category.objects.all()
    safe = Sequrty_question.objects.all()

    if request.method == 'POST':
        #varibals
        fname = None
        lname = None
        category = None
        question =None
        answer =None
        email = None
        username = None
        password = None
        is_added = None
        #get values from form 
        if 'fname' in request.POST: fname = request.POST['fname']
        else: messages.error(request, 'Error in first name !')

        if 'lname' in request.POST: lname = request.POST['lname']
        else: messages.error(request, 'Error in last name !')

        if 'cat' in request.POST: category = Category.objects.get(id=request.POST['cat'])
        else: messages.error(request, 'Error in  category !')

        if 'safe_q' in request.POST: question = Sequrty_question.objects.get(id=request.POST['safe_q'])
        else: messages.error(request, 'Error in question !')

        if 'safe_an' in request.POST: answer = request.POST['safe_an']
        else: messages.error(request, 'Error in answer !')


        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request, 'Error in email !')
        
        if 'user' in request.POST: username = request.POST['user']
        else: messages.error(request, 'Error in username !')
        
        if 'pass' in request.POST: password = request.POST['pass']
        else: messages.error(request, 'Error in password !')
        
        #check values 
        if fname and lname and category and email and username and password:
                #check if user not taken
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'user is already used ')
                else:
                    #check if email not taken
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'email is already used ')
                    else:
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w*)*$"
                        if re.match(patt, email):
                            #add user 
                            user= User.objects.create_user(first_name =fname , last_name=lname , email=email , username=username ,  password=password)
                            user.save()
                            #add user profile
                            userprofile = UserProfile(user=user , favorit_category=category , securty_question=question ,securty_answer=answer)
                            userprofile.save()
                            #Success Message 
                            #messages.success(request, 'your account is created ')
                            username = request.POST['user']
                            password = request.POST['pass']

                            user = auth.authenticate(username=username , password=password)
                            if user is not None:
                                auth.login(request, user)
                                next_page = request.POST.get('next_page' , '/')
                                return HttpResponseRedirect(next_page)
                            else:
                                if request.LANGUAGE_CODE == 'en':
                                    messages.error(request, 'invalid username or password !') 
                                else:
                                    messages.error(request, ' خطا تحقق من صحة المعلومات')

                            is_added = True
                        else:
                            if request.LANGUAGE_CODE == 'en':
                                messages.error(request, 'Invalid email ')
                            else:
                                messages.error(request, ' بريد الالكتروني غير صحيح')
                              
        else:
            if request.LANGUAGE_CODE == 'en':
                messages.error(request, 'Check empty fileds !') 
            else:
                messages.error(request, ' خطا تاكد من تعبئة الحقول')
        
        return render(request, 'accounts/signup.html' ,{
            'fname' : fname,
            'lname' : lname,
            'email' : email,
            'is_added':is_added
        })
    else:
        cat = Category.objects.all()
        safe = Sequrty_question.objects.all()
        return render(request, 'accounts/signup.html' , {'category': cat , 'questions':safe})

# Show and edit User Profile
def profile(request):
    if request.method == 'POST':
        if request.user is not None and request.user.id !=None:
            
            if request.POST['fname'] and request.POST['lname'] and request.POST['email'] and request.POST['user'] :
                request.user.first_name = request.POST['fname'] 
                request.user.last_name = request.POST['lname'] 
                request.user.username = request.POST['user'] 
                
                category = Category.objects.get(id=request.POST['cate'] )
                userprofile =UserProfile.objects.get(user=request.user)
                userprofile.favorit_category = category
                question =Sequrty_question.objects.get(id=request.POST['safe_q'] )
                userprofile.securty_question = question
                userprofile.securty_answer = request.POST['safe_an'] 
                
                userprofile.save()
                request.user.save()
                
                auth.login(request, request.user)

                if request.LANGUAGE_CODE == 'en':
                    messages.success(request, 'changes saved ')
                else:
                    messages.success(request, ' تم حفظ التغييرات')
            else:
                if request.LANGUAGE_CODE == 'en':
                    messages.error(request, 'Check your values and elements ')
                else:
                    messages.error(request, ' خطا تحقق من صحة المعلومات')
                 

        return redirect('profile')

    else:
        if request.user is not None:
            context = None
            if not request.user.is_anonymous:
                userprofile = UserProfile.objects.get(user=request.user)
                cat_list = Category.objects.exclude(id=userprofile.favorit_category.id)
                safe = Sequrty_question.objects.all()
                context={
                    'fname':request.user.first_name,
                    'lname':request.user.last_name,
                    'photo':userprofile.photo,
                    'cat':userprofile.favorit_category,
                    'question':userprofile.securty_question,
                    'answer':userprofile.securty_answer,
                    'category': cat_list,
                    'questions':safe,
                    'email':request.user.email,
                    'user':request.user.username,
                }
            return render(request, 'accounts/profile.html' , context)
        else:
            
            return render(request, 'accounts/profile.html')

# Change user photo
def change_photo(request):
    if request.method == 'POST':
        if request.user is not None and request.user.id !=None:
            userprofile =UserProfile.objects.get(user=request.user)
            uploaded_photo = request.FILES['update_photo']
            userprofile.photo = uploaded_photo
            userprofile.save()

            auth.login(request, request.user)
            return redirect('profile')
            if request.LANGUAGE_CODE == 'en':
                messages.success(request, 'photo has changed ')
            else:
                messages.success(request, ' تم تغيير الصورة')
        else:
            if request.LANGUAGE_CODE == 'en':
                messages.error(request, 'Check your values and elements ')
            else:
                messages.error(request, ' خطا تحقق من صحة المعلومات')
    else:
        return render(request, 'accounts/profile.html')


# Change password 
def change_password(request):
    if request.method == 'POST':
        if request.user is not None and request.user.id !=None:
            if request.user.check_password(request.POST['oldpass']):
                if not request.POST['newpass'].startswith('pbkdf2_sha256$') and request.POST['newpass'] == request.POST['conpass']:
                    request.user.set_password(request.POST['newpass'])
                    request.user.save()
                    auth.login(request, request.user)
        
                if request.LANGUAGE_CODE == 'en':
                    messages.success(request, ' Password chanaged ')
                else:
                    messages.success(request, ' تم تغيير كلمة السر ')
                    return redirect('profile')
            else:
                if request.LANGUAGE_CODE == 'en':
                    messages.error(request, 'Error in password check values ')
                else:
                    messages.error(request, ' خطا في كلمة السر تحقق من صحة المعلومات')
                
        return redirect('change_password')

    else:
        if request.user is not None:
            if not request.user.is_anonymous:
                userprofile = UserProfile.objects.get(user=request.user)
            return render(request, 'accounts/change_password.html' )
        else:
            
            return render(request, 'accounts/change_password.html')

# Forgot Password Functions

# Function no.1 cheack if user is exist
def forgot_password(request):
    if request.method == 'POST':
        user_name = request.POST['userName']
        email = request.POST['email']
        
        if user_name and email and User.objects.filter(username=user_name).exists() and User.objects.filter(email=email).exists():
            select_user = User.objects.get(username=user_name)

            if select_user.username == user_name and select_user.email == email:
                userprofile = UserProfile.objects.get(user=select_user)
                context={
                    'select_user': select_user,
                    'question':userprofile.securty_question

                }
                return render(request, 'accounts/answer_question.html' , context )

            else:
                if request.LANGUAGE_CODE == 'en':
                    messages.error(request, 'invalid email or user name ')
                    return render(request, 'accounts/forget_password.html')
                else:
                    messages.error(request, 'بريد الكتروني او مستخدم غير صحيح')
                    return render(request, 'accounts/forget_password.html')
                
        else:
            if request.LANGUAGE_CODE == 'en':
                messages.error(request, 'invalid email or user name ')
                return render(request, 'accounts/forget_password.html')
            else:
                messages.error(request, 'بريد الكتروني او مستخدم غير صحيح')
                return render(request, 'accounts/forget_password.html')


    else:
        return render(request, 'accounts/forget_password.html')

# Function no.2 Answer security question
def answer_question(request):

    if request.method == 'POST':
        answer = request.POST['safe_an']
        select_user =User.objects.get(username=request.POST['userName'])
        userprofile = UserProfile.objects.get(user=select_user)

        if userprofile.securty_answer == answer:
            context={
                'select_user': select_user,

            }
            return render(request, 'accounts/reseet_password.html' , context )
            
        else:
            if request.LANGUAGE_CODE == 'en':
                messages.error(request, 'your answer is not correct')
                context={
                    'select_user': select_user,
                    'question':userprofile.securty_question

                }
                return render(request, 'accounts/answer_question.html' , context)
            else:
                messages.error(request, 'اجابتك غير صحيحة')
                context={
                    'select_user': select_user,
                    'question':userprofile.securty_question

                }
                return render(request, 'accounts/answer_question.html' , context)
    else:
        return redirect('login')

# Function no.3 Enter new password
def reseet_password(request):
    if request.method == 'POST':
        new = request.POST['newpass']
        con = request.POST['conpass']
        select_user =User.objects.get(username=request.POST['userName'])

        if new and con != None and new == con:
            select_user.set_password(new)
            select_user.save()

            if request.LANGUAGE_CODE == 'en':
                messages.success(request, ' Password chanaged ')
            else:
                messages.success(request, ' تم تغيير كلمة السر ')

            return redirect(login)

        else:
            if request.LANGUAGE_CODE == 'en':
                messages.error(request, 'Passowrd dose not match')
                context={
                    'select_user': select_user,

                }
                return render(request, 'accounts/reseet_password.html' , context)
            else:
                messages.error(request, 'كلمة السر غير مطابقة')
                context={
                    'select_user': select_user,

                }
                return render(request, 'accounts/reseet_password.html' , context)

    else:
        return redirect('login')

# Show  notifications
def notifications(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        user = User.objects.get(username=request.user)
        show = Notification.objects.filter(user=user , movie__is_trend=True)

    context ={
            'shows':show 
            } 

    return render(request, 'accounts/notifications.html ' , context)




#Favourits Functions 

# Show user favourits list
def show_favourits(request):
    context =None
    #del_fav = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo =UserProfile.objects.get(user=request.user)
        mov = userInfo.movie_favorits.all()
        tv = userInfo.tvshow_favorits.all()
        fav=sorted(chain(mov , tv ) , key=lambda obj: obj.publish_date , reverse=True)
        del_fav = True#'del_fav':del_fav
        
        context ={
            'favourits':fav 
            } 

    return render(request, 'accounts/favourits.html ' , context)


# History functions

# Show user history
def show_history(request):
    context =None
    #del_fav = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo =UserProfile.objects.get(user=request.user)
        mov = userInfo.movie_history.all()
        tv = userInfo.tvshow_history.all()
        his=sorted(chain(mov , tv ) , key=lambda obj: obj.publish_date , reverse=True)
        del_fav = True#'del_fav':del_fav
        
        context ={
            'history':his 
            } 

    return render(request, 'accounts/history.html ' , context)

# Clear user hitory
def clear_history(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        userprofile =UserProfile.objects.get(user=request.user)
        userprofile.tvshow_history.clear()
        userprofile.movie_history.clear()

    return render(request, 'accounts/history.html ')


#Notifications Functions

# Show user notifications
def show_notifications(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        user = User.objects.get(username=request.user)
        mov = Movie_Notification.objects.filter(user=user , show__coming_soon=False)
        tv = Tvshow_Notification.objects.filter(user=user , show__coming_soon=False)
        notf=sorted(chain(mov , tv ), key=lambda obj: obj.read )
        return render(request, 'accounts/notifications.html ' , { 'notifications':notf })
    else:
        messages.error(request, 'you must be logged in ')
    
    return render(request, 'accounts/notifications.html')

# Clear user notifications
def clear_notifications(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        user = User.objects.get(username=request.user)
        mov = Movie_Notification.objects.filter(user=user)
        mov.delete()
        tv = Tvshow_Notification.objects.filter(user=user)
        tv.delete()
        return redirect(show_notifications)
    else:
        messages.error(request, 'you must be logged in ')
    return render(request, 'accounts/notifications.html')

        
        
    
    