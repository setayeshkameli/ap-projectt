from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SigninForm,LoginForm
from django.contrib import messages

def home(request):
    pass
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form})
def signup(request):
    form=SigninForm()
    if request.method=="POST":
        form=SigninForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request,'signin.html',{'form':form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_superuser:
                    return redirect('admin_panel')
                else:
                    return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login credentials.'})
    else:
        form = LoginForm()
        redirect()
    return render(request, 'login.html', {'form': form})
   

def logout_view(request):
    logout(request)
    messages.success(request,('با موفقیت خارح شدید'))
    return redirect('home')
