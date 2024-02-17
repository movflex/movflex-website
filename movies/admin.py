from django.contrib import admin
from .models import Movie , Comment 
from django.utils.html import format_html
# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    
    def poster_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px;max-height:150px;border: 4px solid;border-radius: 10px;">'.format(obj.poster.url))
    poster_tag.short_description = 'poster'
    list_display = ['poster_tag','name' , 'season', 'imbd' , 'release_year' , 'category' , 'channel' , 'is_trend']
    list_editable = ['is_trend' ]
    list_filter = ['category' , 'release_year' , 'channel' , 'language' , 'casts']
    search_fields =['name']

    def delete_model(self, request, obj):
        if obj.poster:
            photo_path = obj.poster.path
            if os.path.exists(photo_path):
                os.remove(photo_path)
                super().delete_model(request, obj)

    




class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_nam', 'movie_name' , 'comment_date']
    list_filter = ['movie_name']
    search_fields =['user_nam']

admin.site.register(Movie , MoviesAdmin)
admin.site.register(Comment , CommentAdmin )


