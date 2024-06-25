from django.urls import path,include
from .views import *
urlpatterns = [    
   # path('',home,name='home'),
    path('signin/',signin,name='signin'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout')
    #path('manage/',manage,name='manage')
]