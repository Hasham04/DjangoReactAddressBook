from django.urls import path
from .import views

urlpatterns = [

    path('home/',views.list,name='list'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
]
