from django.db import models
#from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

class Pages(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)    
    page = models.CharField(max_length=250, verbose_name='Səhifənin adı')    
    page_url = models.CharField(max_length=250, verbose_name='Alt səhifə (url)')    
    

    def __str__(self):
        return self.page

class Post(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)  
    page_id = models.ForeignKey(Pages, on_delete=models.CASCADE)  
    title = models.CharField(max_length=250, verbose_name='Başlıq')
    slug = models.SlugField(max_length=250,verbose_name='Slug')
    picture = models.ImageField(upload_to='img/',blank=True,verbose_name='Şəkil')
    created_at = models.DateTimeField(verbose_name='İndiki vaxt')
    content = RichTextUploadingField() #HTMLField()
    def __str__(self):
        return self.title

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.picture.url))
    image_tag.short_description = 'Image'





    






    """class About(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)    
    title = models.CharField(max_length=250, verbose_name='Başlıq')    
    picture = models.ImageField(upload_to='img/',blank=True,verbose_name='Şəkil')    
    content = RichTextUploadingField() #HTMLField()

    def __str__(self):
        return self.title
    
    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.picture.url))
    image_tag.short_description = 'Image'


class Contact(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)    
    title = models.CharField(max_length=250, verbose_name='Başlıq')    
    picture = models.ImageField(upload_to='img/',blank=True,verbose_name='Şəkil')    
    content = RichTextUploadingField() #HTMLField()

    def __str__(self):
        return self.title
    
    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.picture.url))
    image_tag.short_description = 'Image'"""