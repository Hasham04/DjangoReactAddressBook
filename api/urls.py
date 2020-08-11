from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('address-list/', views.addressList, name="address-list"),
	path('address-detail/<str:pk>/', views.addressDetail, name="address-detail"),
	path('address-create/', views.addressCreate, name="address-create"),
	path('address-update/<str:pk>/', views.addressUpdate, name="address-update"),
	path('address-delete/<str:pk>/', views.addressDelete, name="address-delete"),
]
