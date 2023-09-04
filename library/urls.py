from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('author.urls')),
    path('publisher/', include('publisher.urls')),
    path('book/', include('book.urls')),
    path('faker/', include('fake_data.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
