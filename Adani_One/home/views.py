from django.shortcuts import render
from .models import SignUp
from home.sign_up import restrict_character,check_password_length,salting

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

        # Name Varification Code 
        restrict_character(name)
        if(restrict_character(name) == False):
            message = "Invalid Name"
            return render(request,'error.html',{"error_text" : message})
            
        # Email Verification Code
        signups = SignUp.objects.all()
        email_same = False

        for i in signups:
            if(i.email == email):
                email_same = True
                    
        if(email_same == True):
            message = "Email is already registered"
            return render(request,'error.html',{'error_text' : message})

        # Password Verification Code 
        if(password == repassword): 
            if(check_password_length(password) == True):
                salted_passcode = salting(password)
                signup_entry = SignUp(name=name, email=email, contact=contact, password=salted_passcode)
                signup_entry.save()
                return render(request,'success.html')
            else:
                message = "Password is Improper, Should be between 8 - 20 Characters"
                return render(request,'error.html',{'error_text' : message})
            
        else:
            message = "Incorrect Password"
            return render(request,'error.html',{'error_text' : message})

    
    return render(request,'sign_up.html')

def login(request):
    return render(request,'login.html')

def test(request):
    return render(request, 'test.html')