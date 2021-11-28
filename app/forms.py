from django import forms
from .models import *
from django.contrib.auth.models import User
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','author','cover','price')

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','password')


