from django.contrib import admin
from .models import UserProfile , Movie_Notification , Tvshow_Notification
from django.utils.html import format_html

# Register your models here.

class AccountsAdmin(admin.ModelAdmin):

    def photo_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px;max-height:150px;border: 4px solid;border-radius: 10px;">'.format(obj.photo.url))
    photo_tag.short_description = 'photo'
    list_display = ['photo_tag','user' , 'favorit_category']
    search_fields =['user']


class Movie_NotificationAdmin(admin.ModelAdmin):
    list_display = ['user' , 'read']
    search_fields =['user']

class Tvshow_NotificationAdmin(admin.ModelAdmin):
    list_display = ['user' , 'read']
    search_fields =['user']



admin.site.register(UserProfile ,AccountsAdmin)
admin.site.register(Movie_Notification ,Movie_NotificationAdmin)
admin.site.register(Tvshow_Notification ,Tvshow_NotificationAdmin)