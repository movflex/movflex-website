from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from tvshows.models import Tvshow
from pages.models import Category , Sequrty_question
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='photos/profile' , null=True , blank=True)

    movie_favorits = models.ManyToManyField(Movie , related_name="movie_favorits")

    tvshow_favorits = models.ManyToManyField(Tvshow , related_name="tvshow_favorits")

    movie_history = models.ManyToManyField(Movie , related_name="movie_history")

    tvshow_history = models.ManyToManyField(Tvshow , related_name="tvshow_history")


    favorit_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True) 

    securty_question = models.ForeignKey(Sequrty_question , on_delete=models.PROTECT , null=True)

    securty_answer = models.TextField( null=True)

    def __str__(self):
        return self.user.username

class Movie_Notification(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    show = models.ForeignKey(Movie , on_delete=models.CASCADE)

    read = models.BooleanField( default=False)

class Tvshow_Notification(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    show = models.ForeignKey(Tvshow , on_delete=models.CASCADE)

    read = models.BooleanField( default=False)
