from django.contrib import admin
from .models import Tvshow , Comment 
from django.utils.html import format_html
# Register your models here.
class TvshowAdmin(admin.ModelAdmin):

    def poster_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px;max-height:150px;border: 4px solid;border-radius: 10px;">'.format(obj.poster.url))
    poster_tag.short_description = 'poster'
    list_display = ['poster_tag','name' , 'season', 'imbd' , 'release_year' , 'category' , 'channel' , 'is_trend']
    list_editable = ['is_trend' ]
    list_filter = ['category' , 'release_year' , 'channel' , 'language' , 'casts']
    search_fields =['name']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_nam', 'tvshow_name' , 'comment_date']
    list_filter = ['tvshow_name']
    search_fields =['user_nam']

admin.site.register(Tvshow , TvshowAdmin)
admin.site.register(Comment , CommentAdmin )
