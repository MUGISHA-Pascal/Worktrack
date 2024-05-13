from .models import signupdatabase
from django import forms
from django.forms import ModelForm
class signupform(ModelForm):
    class Meta:
        model=signupdatabase
        fields="__all__"
    
    