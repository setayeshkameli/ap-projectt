from django import forms
from.models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class SigninForm(UserCreationForm):
  #  class Meta:
#       model=Users
#       fields=['Username','Fullname','Email','Password','Phone_number']
#class LoginForm(forms.Form):
#    username = forms.CharField( label='Username or Email')
 #   password = forms.CharField(widget=forms.PasswordInput, label='Password')

class SigninForm(UserCreationForm):
  Fullname=forms.CharField(label='',max_length=255,widget=forms.TextInput(attrs={'class':'form-control' ,"placeholder":"نام و نام خانوادگی"}))
  Username=forms.CharField(label='',max_length=255,widget=forms.TextInput(attrs={'class':'form-control' ,"placeholder":"نام کاربری"}))
  Email=forms.CharField(label='',max_length=255,widget=forms.TextInput(attrs={'class':'form-control' ,"placeholder":"ایمیل"}))
  Password=forms.CharField(label='',max_length=255,widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"رمز عبور ثابت"}))
  class Meta:
    model =User
    fields=['Username','Fullname','Email','Password']