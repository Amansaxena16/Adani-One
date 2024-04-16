from django.shortcuts import render

def index(request):
    context = {'page' : 'Adani One'}
    return render(request, 'index.html',context)

def vip_services(request):
    context = {'page' : 'VIP Services'}
    return render(request, 'vip_services.html',context)

def sign_up(request):
    return render(request,'sign_up.html')

def login(request):
    return render(request,'login.html')

def test(request):
    return render(request, 'test.html')