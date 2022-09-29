from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
# Create your models here.


class Blog(models.Model):
    creater_name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='blogs')
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=70,verbose_name="Title")
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    description = FroalaField()
    slug = models.SlugField(max_length=1000, null=False, unique=True, db_index=True, blank=True, editable=False)
    upload_to = models.DateTimeField(auto_now=True)
    isFeatured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title 

    def save(self , *args, **kwargs):
        self.slug = create_slug(self.title)
        super(Blog, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=150)

  

   


    


