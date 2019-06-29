from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404 ,redirect
from django.utils import timezone
from .models import Twice
from .models import Blog

def twice(request):
    members=Twice.objects.filter(nationality='JP')
    return render(request, 'home.html' ,{'japanese':members})
def twice2(request):
    members=Twice.objects.filter(position__icontains='서브보컬')
    return render(request, 'home2.html' ,{'sub_vocals':members})
    
def blog(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator=Paginator(blog_list,3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'blog.html', {'blogs':blogs},{'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))