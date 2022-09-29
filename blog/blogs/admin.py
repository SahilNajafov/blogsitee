from django.contrib import admin
from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    search_fields = ("title","subject",)
    readonly_fields = ("slug",)

admin.site.register(Blog,BlogAdmin)
