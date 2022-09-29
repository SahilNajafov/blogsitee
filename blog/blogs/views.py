from ast import Delete
from multiprocessing import context
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from . import forms
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db import models

# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request,'index.html', context)

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def featured(request):
    context = {
        "blogs": Blog.objects.filter(isFeatured=True)
    }
    return render(request, 'featured.html',context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request,'blog_details.html', {
        "blog" : blog
    })

def add_blog(request):
    form = forms.BlogForm()

    if request.method == 'POST':
        form = forms.BlogForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('index')
        else:
            form = forms.BlogForm(request.POST, request.FILES)
    context = {
        'form': form,#forms.BlogForm
    }
    return render(request, 'add_blog.html', context)

def created_blogs(request):
    context = {
        'blog_obj': Blog.objects.filter(user = request.user)
    }
    return render(request, 'created_blogs.html',context)

@login_required(login_url="login")
def blog_edit(request,slug):
    # blog_objs = Blog.objects.get(slug = slug)
    blog_objs = get_object_or_404(Blog, slug = slug)

    # if blog_objs.user != request.user:
    #     return redirect('/')

    # initial_dict = {
    #     'title': blog_objs.title,
    #     'subject': blog_objs.subject,
    #     'description': blog_objs.description,
    #     'creater_name': blog_objs.creater_name,
    #     'image': blog_objs.image
    # }
    # form = forms.BlogForm(initial = initial_dict)
    if request.method == 'POST':
        form = forms.BlogForm(request.POST, request.FILES, instance = blog_objs)
        if form.is_valid():
            instnce = form.save(commit=False)
            instnce.user = request.user
            instnce.save()
            return redirect('index')
    else:
        form = forms.BlogForm(instance = blog_objs)
        
    context = {
        'blog_objs': blog_objs,
        'form': form,
    }
    return render(request, 'edit_blog.html', context)

@login_required(login_url="login")
def blog_delete(request,id):
    try:
        blog_objs = Blog.objects.get(id = id)
        if blog_objs.user == request.user:
            blog_objs.delete()
    except Exception as e:
        print(e)
    return redirect('created_blogs')
