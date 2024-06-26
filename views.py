from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SigninForm
from django.contrib import messages
from .models import Product

def home(request):
    return render(request,'home.html',{})
def signin(request):
    form=SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect('home')
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                if user.is_superuser:
                    return redirect('manage') 
                else:
                    return redirect('home') 
            else:
                return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,('با موفقیت خارح شدید'))
    return redirect('home')
def manage_view(request):
    return render(request,'manage.html')

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sugar = request.POST.get('sugar')
        coffee = request.POST.get('coffee')
        flour = request.POST.get('flour')
        chocolate = request.POST.get('chocolate')
        vertical = request.POST.get('vertical')
        price = request.POST.get('price')
        new_product = Product(
            name=name,
            sugar=sugar,
            coffee=coffee,
            flour=flour,
            chocolate=chocolate,
            vertical=vertical,
            price=price
        )
        new_product.save()
        messages.success(request, 'محصول جدید با موفقیت اضافه شد.')
        return redirect('add_product')
    else:
        return render(request, 'add_product.html')

