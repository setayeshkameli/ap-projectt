from django.urls import path,include
from .views import *

urlpatterns = [    
    path('',home,name='home'),
    path('signin/',signin,name='signin'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('manage/',manage_view,name='manage'),
    path('add_product/',add_product,name='add_product')

]