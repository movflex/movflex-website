from django.contrib import admin
from .models import Channel
from django.utils.html import format_html

# Register your models here.
class ChannelsAdmin(admin.ModelAdmin):
    def logo_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px;max-height:150px;border: 4px solid;border-radius: 10px;">'.format(obj.logo.url))
    logo_tag.short_description = 'logo'
    list_display = ['logo_tag','name']
    search_fields =['name']


admin.site.register(Channel , ChannelsAdmin)