from django.db import models
from datetime import date, datetime
from django.forms import DateField
from channels.models import Channel
from cast_and_crew.models import Cast,Director,Writer
from pages.models import Category,Language ,Release_year ,Tag
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.



class Movie(models.Model):
    #primry 
    name = models.CharField(max_length=80)
    season = models.IntegerField()
    coming_soon = models.BooleanField( default=False )
    poster = models.ImageField(upload_to='photos/posters/movies' )
    watch_url = models.TextField(default="google.com")
    description = models.TextField()
    description_ar = models.TextField(default='none')
    imbd = models.DecimalField( max_digits=2, decimal_places=1)
    number_views = models.IntegerField()
    gross = models.IntegerField()
    typee = models.TextField(default="Movies", editable=False)
    

    #relation
    language = models.ForeignKey( Language , on_delete=models.PROTECT)
    category = models.ForeignKey( Category , on_delete=models.PROTECT)
    channel = models.ForeignKey(Channel , on_delete=models.PROTECT)
    casts = models.ManyToManyField(Cast , blank=True  )
    director = models.ManyToManyField(Director , blank=True  )
    writer = models.ManyToManyField(Writer , blank=True  )
    release_year = models.ForeignKey( Release_year , on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag , blank=True , related_name="movies_tags")

    #defualt
    is_trend = models.BooleanField( default=False )
    publish_date = models.DateTimeField( default=datetime.now )
    slug = models.SlugField(blank=True , null=True , unique=True)

    # to insert slug field from name field
    def save(self,*args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.season}")
        super(Movie, self).save(*args, **kwargs)


    def __str__(self):
        return self.name 

    class Meta:
        ordering =['release_year']


class Comment(models.Model):

    user_nam = models.ForeignKey(User , on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie , on_delete=models.CASCADE)
    comment = models.TextField()
    evalute = models.DecimalField( max_digits=2, decimal_places=1)
    comment_date = models.DateTimeField( default=datetime.now ) 








    




