from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','image_tag']
    list_display_links = ['title']
    list_filter = ['created_at']
    search_fields = ['title']
    #fields = ['title','picture','created_at']



    class Meta:
        model = Post
"""
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title']
    #fields = ['title','picture','created_at']



    class Meta:
        model = About

class ContactAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title']
    #fields = ['title','picture','created_at']



    class Meta:
        model = Contact
"""

class PageAdmin(admin.ModelAdmin):
    list_display = ['page']
    list_display_links = ['page']
    list_filter = ['page']
    search_fields = ['page']
    #fields = ['title','picture','created_at']



    class Meta:
        model = Pages




admin.site.register(Post,PostAdmin)
#admin.site.register(About,AboutAdmin)
#admin.site.register(Contact,ContactAdmin)
admin.site.register(Pages,PageAdmin)