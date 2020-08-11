from django.shortcuts import render


def list(request):
	return render(request,'frontend/list.html',{})

def login(request):
	return render(request,'frontend/login.html',{})

def register(request):
	return render(request,'frontend/register.html',{})