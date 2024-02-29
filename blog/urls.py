from django.contrib import admin
from django.urls import include, path,re_path

from polls.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('polls.urls',namespace="index") ),
    path('index', include('polls.urls',namespace="index")),    
    path('post/<slug:slug>', include('polls.urls',namespace="post")) ,
    path('about/<slug:slug>', include('polls.urls',namespace="about")),
    path('contact', include('polls.urls',namespace="contact")),
    #path('tinymce/', include('tinymce.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    

]
