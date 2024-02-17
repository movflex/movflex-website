from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns 



urlpatterns = [
    path('il8n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('' , include('pages.urls')),
    path('accounts/' , include('accounts.urls')),
    path('movies/' , include('movies.urls')),
    path('channels/' , include('channels.urls')),
    path('tvshows/' , include('tvshows.urls')),
    path('top_rank/' , include('top_rank.urls')),
    

) + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
