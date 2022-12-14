from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={  'type':"email",'id':"form3Example3@nitk.edu.in",'class':'form-control'}),

        }


class LoginForm(AuthenticationForm):
    # <input type="email" id="typeEmailX-2" class="form-control form-control-lg" />
   username = UsernameField(widget=forms.EmailInput(attrs={'type':"email" ,'id':'typeEmailX-2' ,'class':"form-control form-control-lg mb-2"}))#we are doing it simply because we need to write the bootstrap class
#    username = UsernameField(widget=forms.EmailInput(attrs={'autofocus':True,'class':'form-control'}))#we are doing it simply because we need to write the bootstrap class
   password = forms.CharField(
    label = _("Password "),
    strip=False, 
    widget = forms.PasswordInput(attrs={
        'autocomplete':'current-password',
        'class':"form-control form-control-lg mb-2"
        })
    )
