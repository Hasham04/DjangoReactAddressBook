from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AddressSerializer
from .models import AddressBook
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/address-list/',
		'Detail View':'/address-detail/<str:pk>/',
		'Create':'/address-create/',
		'Update':'/address-update/<str:pk>/',
		'Delete':'/address-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def addressList(request):
	user_id = request.user.id
	addresses = AddressBook.objects.filter(user_id=user_id).order_by('-id')
	serializer = AddressSerializer(addresses, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def addressDetail(request, pk):
	addresses = AddressBook.objects.get(id=pk)
	serializer = AddressSerializer(addresses, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def addressCreate(request):
	serializer = AddressSerializer(data=request.data)
	
	print(serializer.is_valid())
	if serializer.is_valid():
		serializer.save()
		#print("TRUE")

		

	return Response(serializer.data)

@api_view(['POST'])
def addressUpdate(request, pk):
	address = AddressBook.objects.get(id=pk)
	serializer = AddressSerializer(instance=address, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def addressDelete(request, pk):
	address = AddressBook.objects.get(id=pk)
	address.delete()

	return Response('Item succsesfully delete!')



