from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering =['name']

    #to count number of movies in each gener
    def movie_count(self):
        return self.movie_set.all().count()

    #to count number of tvshows in each gener
    def tvshow_count(self):
        return self.tvshow_set.all().count()
    

class Language(models.Model):
    name = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering =['name']

class Release_year(models.Model):
    year = models.IntegerField()

    class Meta:
        ordering =['-year']

    def __str__(self):
        return str(self.year)

    #to count number of movies in each year
    def movie_count(self):
        return self.movie_set.all().count()

    #to count number of tvshows in each year
    def tvshow_count(self):
        return self.tvshow_set.all().count()
    
    
class Tag(models.Model):

    titel = models.TextField()

    slug = models.SlugField(blank=True , null=True)

    # to insert slug field from name field
    def save(self,*args, **kwargs):
        self.slug = slugify(self.titel)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.titel

class Sequrty_question(models.Model):

    name = models.TextField()
    name_ar = models.TextField()

    def __str__(self):
        return self.name
