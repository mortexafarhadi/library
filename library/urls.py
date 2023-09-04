from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('site_setting.urls')),
    path('admin/', admin.site.urls),
    path('author/', include('author.urls')),
    path('publisher/', include('publisher.urls')),
    path('order/', include('order.urls')),
    path('faker/', include('fake_data.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
