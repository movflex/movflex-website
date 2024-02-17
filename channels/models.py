from django.db import models
from django.utils.text import slugify
# Create your models here.

class Channel(models.Model):
    
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='photos/logo' )

    slug = models.SlugField(blank=True , null=True)

    # to insert slug field from name field
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name 

    #to count number of movies in each channel
    def movie_count(self):
        return self.movie_set.all().count()

    #to count number of tvshows in each channel
    def tvshow_count(self):
        return self.tvshow_set.all().count()
    
