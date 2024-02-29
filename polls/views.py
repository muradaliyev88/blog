from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator


def index(request):
    pages= Pages.objects.all()    
    data = Post.objects.select_related("page_id").filter(page_id_id__page_url="index")    
    data2 = Post.objects.order_by("slug")        
    page = Paginator(data2, 1)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    print("$$$$$",pages)
    return render(request,"main.html",{"data":data,"page_obj":page_obj,"pages":pages})


def post(request,slug=None):
    pages= Pages.objects.all()
    data = get_object_or_404(Post.objects.filter(slug__contains=slug).values())
    data2 = Post.objects.select_related("page_id").filter(page_id_id__page_url="index")[::-3]
    print(data,"data2$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
    return render(request,"post.html",{"data":data,"data2":data2,"pages":pages})




def about(request,slug=None):    
    data = get_object_or_404(Post.objects.select_related("page_id").filter(page_id_id__page_url=slug))    
    print(data,"data")
    pages= Pages.objects.all()
    return render(request,"about.html",{"data":data,"pages":pages})

def contact(request):
    pages= Pages.objects.all()
    data = Post.objects.select_related("page_id").filter(page_id_id__page_url="contact").values()
    print("data",data[0]['picture'])
    return render(request,"contact.html",{"data":data[0],"pages":pages})