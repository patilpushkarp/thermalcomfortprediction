#-*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User
from myapp.models import Profiles
from django.utils.translation import ugettext_lazy as _

class Signup(forms.ModelForm):
   
   class Meta:
      model = Profiles
      fields = ('username', 'password', 'name', 'email', 'age', 'gender', 'ta_m', 'va_m')
   

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = Profiless.objects.filter(name = username)
      
      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      return username
