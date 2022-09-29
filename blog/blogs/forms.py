from django import forms
from . import models
from django.forms import ModelForm
from froala_editor.widgets import FroalaEditor


class BlogForm(forms.ModelForm):
#     description = forms.CharField(widget=FroalaEditor(options={
#     'toolbarInline': True,
#   }))

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-input'
    class Meta:
        model = models.Blog
        fields = [
        'title',
        'subject',
        'description',
        'creater_name',
        'image',
        'isFeatured'
        ]