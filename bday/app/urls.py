from django.contrib import admin
from django.urls import path
from mainpage.views import mainpage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage_views, name='mainpage'),
]