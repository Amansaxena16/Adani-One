from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import SignUp

def index(request):
    context = {'page' : 'Adani One'}
    return render(request, 'index.html',context)

def vip_services(request):
    context = {'page' : 'VIP Services'}
    return render(request, 'vip_services.html',context)

def sign_up(request):
    if(request.method == "POST"):
        name = request.POST.get('name')     
        email = request.POST.get('email')     
        contact = request.POST.get('contact')     
        password = request.POST.get('password')     
        repassword = request.POST.get('repassword') 

        if(password == repassword):
            signup_entry = SignUp(name=name, email=email, contact=contact, password=password, re_password=repassword)
            signup_entry.save()
            return render(request,'success.html')
        
        else:
            return render(request,'error.html')

    return render(request,'sign_up.html')

def login(request):
    return render(request,'login.html')

def test(request):
    return render(request, 'test.html')