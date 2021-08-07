from os import name
from django import urls
#from detect import detect_fruit
#from delete_image import deletename
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
import webs
#import detect
import delete_image


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload,name='upload'),
    path('delete/',delete_image.deletefile, name='deletefile'),
    path('home/',views.home, name='home'),
    path('upimg/',views.upimg, name='upimg'),
    path('profile/',views.profile, name='profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)