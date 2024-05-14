from .models import *
from django import forms
from django.forms import ModelForm
class signupform(ModelForm):
    class Meta:
        model=signupdatabase
        fields="__all__"
class department1form(ModelForm):
    class Meta:
        model=department1
        fields="__all__"    
    
