from django import forms
from django.forms import ModelForm, Form
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AdsForm(ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields ='__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['to_post', 'from_user', 'text']
