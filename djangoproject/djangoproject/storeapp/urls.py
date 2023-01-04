from . import views
from django.urls import path

app_name='storeapp'

urlpatterns=[
    path('',views.demo,name='demo'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout,name='logout'),
    path('avail',views.avail,name='avail'),
    path('getdata',views.getdata,name='getdata'),
]