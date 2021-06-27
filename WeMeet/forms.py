from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomRegFormSchool(UserCreationForm):
    # school_email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields =['username','email','password1','password2']