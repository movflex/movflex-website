from django.contrib import admin
from .models import Cast,Director,Writer
from django.utils.html import format_html
import os
# Register your models here.
class CastAdmin(admin.ModelAdmin):

    def photo_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px;max-height:150px;border: 4px solid;border-radius: 10px;">'.format(obj.photo.url))
    photo_tag.short_description = 'photo'
    list_display = ['photo_tag','name' ]
    search_fields =['name']

    def delete_model(self, request, obj):
        if obj.photo:
            photo_path = obj.photo.path
            if os.path.exists(photo_path):
                os.remove(photo_path)
                super().delete_model(request, obj)

class DirectorAdmin(admin.ModelAdmin):

    def photo_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px;max-height:150px;border: 4px solid;border-radius: 10px;">'.format(obj.photo.url))
    photo_tag.short_description = 'photo'
    list_display = ['photo_tag','name' ]
    search_fields =['name']

    def delete_model(self, request, obj):
        if obj.photo:
            photo_path = obj.photo.path
            if os.path.exists(photo_path):
                os.remove(photo_path)
                super().delete_model(request, obj)

class WriterAdmin(admin.ModelAdmin):

    def photo_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px;max-height:150px;border: 4px solid;border-radius: 10px;">'.format(obj.photo.url))
    photo_tag.short_description = 'photo'
    list_display = ['photo_tag','name' ]
    search_fields =['name']

    def delete_model(self, request, obj):
        if obj.photo:
            photo_path = obj.photo.path
            if os.path.exists(photo_path):
                os.remove(photo_path)
                super().delete_model(request, obj)


admin.site.register(Cast , CastAdmin)
admin.site.register(Director , DirectorAdmin)
admin.site.register(Writer , WriterAdmin)
