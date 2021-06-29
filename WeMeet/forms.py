from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomRegFormSchool(UserCreationForm):
    # school_email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields =['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(CustomRegFormSchool, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'SCHOOL NAME'
        self.fields['email'].widget.attrs['placeholder'] = 'EMAIL'
        self.fields['password1'].widget.attrs['placeholder'] = 'PASSWORD'
        self.fields['password2'].widget.attrs['placeholder'] = 'CONFIRM PASSWORD'


class CustomRegFormStudent(UserCreationForm):
    # school_email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields =['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(CustomRegFormStudent, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'STUDENT NAME'
        self.fields['email'].widget.attrs['placeholder'] = 'EMAIL'
        self.fields['password1'].widget.attrs['placeholder'] = 'PASSWORD'
        self.fields['password2'].widget.attrs['placeholder'] = 'CONFIRM PASSWORD'