from django import forms
from django.forms import ModelForm
from .models import *

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'