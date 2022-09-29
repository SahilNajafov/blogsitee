from django.utils.text import slugify



# Python3 code to demonstrate
# generating random strings 
# using random.choices()
import string
import random

def random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return res

  
def create_slug(text):
    new_slug = slugify(text)
    from blogs.models import Blog
    if Blog.objects.filter(slug = new_slug).first():
        return create_slug(text + random_string(5))
    return new_slug