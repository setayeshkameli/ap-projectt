from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SigninForm
from django.contrib import messages
from .models import Product
from .models import Storage, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
def home(request):
    products=Product.objects.all()
    best_sellers=Product.objects.order_by('-sales')[:12]
    return render(request,'home.html',{'products':products,'best_sellers':best_sellers})

           
def signin_view(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form =SigninForm()
    return render(request, 'signin.html', {'form': form})
def login_view(request):
    if request.method=='GET':
        return render(request, 'login.html',{})
    elif request.method == 'POST':
        username_or_email=request.POST.get('username_or_email')
        password=request.POST.get('password')
        try:
           user=User.objects.get(username=username_or_email)
        except:
            user=User.objects.get(email=username_or_email)
        if user is not None and user.check_password(password):
            login(request,user)
            if user.is_superuser:
               return redirect('manage')
            else:
               return redirect('home')
        return render(request, 'login.html',{})
          
def logout_view(request):
    logout(request)
    messages.success(request,('با موفقیت خارح شدید'))
    return redirect('home')
def manage_view(request):
    return render(request,'manage.html')

def manage_inventory(request):
    storage=Storage.objects.all()
    return render(request,'manage_inventory.html',{'storage':storage})

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sugar = request.POST.get('sugar')
        coffee = request.POST.get('coffee')
        flour = request.POST.get('flour')
        chocolate = request.POST.get('chocolate')
        vertical = request.POST.get('vertical')
        price = request.POST.get('price')
        image=request.POST.get('image')
        new_product = Product(
            name=name,
            sugar=sugar,
            coffee=coffee,
            flour=flour,
            chocolate=chocolate,
            vertical=vertical,
            price=price,
            image=image
        )
        new_product.save()
        messages.success(request, 'محصول جدید با موفقیت اضافه شد.')
        return redirect('add_product')
    else:
        return render(request, 'add_product.html')

def purchase_view(request):
    return render(request,'purchasehistory.html')
@login_required
def cart_view(request):
 return render(request,'cart.html')

def products_view(request):
   return render(request,'products.html',{'products':Product.objects.all()})





