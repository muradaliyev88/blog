from django.urls import path, re_path

from . import views
app_name = 'polls'



urlpatterns = [
   
    path('', views.index, name='index'),   
    path('index', views.index, name='index'),
    path('post/<slug:slug>', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('<slug:slug>', views.about, name='about'),
       
]

