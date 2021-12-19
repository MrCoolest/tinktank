from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('userlogin',views.userLogin,name='userlogin'),
    path('userlogout',views.userLogout,name='userlogout'),
    path('search',views.search,name='search')
]