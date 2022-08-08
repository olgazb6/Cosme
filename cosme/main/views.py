from django.shortcuts import render
from catalog.models import Catalog
from shop.models import Blog

# Create your views here.

def index(request):
    product = Catalog.objects.order_by('-created_on')[:4]
    blog_item = Blog.objects.order_by('-created_on')[:4]
    context = {
        'product': product,
        'blog_item' : blog_item,
    }
    return render(request,'index.html', context)

def about(request):
    return render(request,'about.html')

def delivery(request):
    return render(request,'delivery.html')

def contacts(request):
    return render(request,'contacts.html')
