from django.contrib import admin
from django.urls import path
from mainpage.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', mainpage_views, name='mainpage'),
    path('', product_list, name='product_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)