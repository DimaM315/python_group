from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import zero_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('feed/', include('feed.urls')),
    path('articles/', include('articles.urls')),
    path('tasks/', include('tasks.urls')),
    path('', zero_path),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
