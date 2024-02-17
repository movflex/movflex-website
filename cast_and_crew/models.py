from django.db import models
from django.utils.text import slugify
# Create your models here.

class Cast(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='photos/cast_photos')
    age = models.IntegerField()
    country = models.CharField(max_length=80)

    slug = models.SlugField(blank=True , null=True)

    # to insert slug field from name field
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Cast, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='photos/director_photos')
    age = models.IntegerField()
    country = models.CharField(max_length=80)
    job = models.TextField(default="Director", editable=False)

    slug = models.SlugField(blank=True , null=True)

    # to insert slug field from name field
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Director, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='photos/writer_photos')
    age = models.IntegerField()
    country = models.CharField(max_length=80)
    job = models.TextField(default="Writer", editable=False)

    slug = models.SlugField(blank=True , null=True)

    # to insert slug field from name field
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Writer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


    

    
  
    