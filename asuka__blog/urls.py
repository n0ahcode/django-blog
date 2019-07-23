from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ixtab/', admin.site.urls),
    path('card/', include('card_app.urls')),
    path('post/', include('post_app.urls')),
    path('summernote/', include('django_summernote.urls')),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)