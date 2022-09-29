
from django.urls import path
from .views import *

urlpatterns = [
    path('' , index , name="index"),
    path('index/' , index, name="blogs"),
    path('blogs/<slug:slug>' , blog_details , name="blog_details"),
    path("add-blog/", add_blog, name="add_blog"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("featured/", featured, name="featured"),
    path("created-blogs/", created_blogs, name="created_blogs"),
    path("blog_delete/<id>", blog_delete, name="blog_delete"),
    path("blog-edit/<slug>/", blog_edit, name="blog_edit"),
]