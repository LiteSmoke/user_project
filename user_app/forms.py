from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import UserInfo

class UserForm(ModelForm):

    # username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (fname, f) in self.fields.items():
            f.widget.attrs.update({'class':'form-control'})

            # if fname == "password":
            #     f.widget.attrs.update(type='password')

        # self['password'].field.widget.attrs.update({'type':'password'})

    class Meta():
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserInfoForm(ModelForm):

    profile_icon = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update({'required':False, 'hidden':True})
        # self.fields['profile_icon'].widget.attrs.update({'required':False})

        for (fname, f) in self.fields.items():

            if fname != "user":
                f.widget.attrs.update({'class':'form-control'})

    class Meta():
        model = UserInfo
        fields = '__all__'

class UserProfileForm(ModelForm):

    class Meta():
        model = UserInfo
        fields = '__all__'
