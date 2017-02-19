
from django.conf.urls import url, include
from django.contrib import admin
from comment.views import comment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('user.urls')),
    url(r'^post/', include('feeds.urls')),
    url(r'^(?P<id>\d+)/comment/', comment),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


