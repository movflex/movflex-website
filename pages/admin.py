from django.contrib import admin
from .models import Category,Release_year , Language , Tag ,Sequrty_question
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' ]
    search_fields =['name']

class Release_yearAdmin(admin.ModelAdmin):
    list_display = ['year' ]
    list_filter = ['year']

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name' ]
    list_filter = ['name']

class TagsAdmin(admin.ModelAdmin):
    list_display = ['titel']
    search_fields =['titel']

class Sequrty_questionAdmin(admin.ModelAdmin):
    list_display = ['name' ]
    list_filter = ['name']

admin.site.register(Category , CategoryAdmin)
admin.site.register(Release_year , Release_yearAdmin)
admin.site.register(Language , LanguageAdmin)
admin.site.register(Tag , TagsAdmin )
admin.site.register(Sequrty_question , Sequrty_questionAdmin)
