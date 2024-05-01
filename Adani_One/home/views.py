from django.shortcuts import render
from .models import SignUp
from .sign_up import *
from cryptography.fernet import Fernet, InvalidToken
from django.core.mail import send_mail

with open("Key.key","br") as f:
    key = f.read()

cipher_suite = Fernet(key)

def index(request):
    context = {'page' : 'Adani One'}
    return render(request, 'index.html',context)

def vip_services(request):
    context = {'page' : 'VIP Services'}
    return render(request, 'vip_services.html',context)

def sign_up(request):
    if(request.method == "POST"):
        # fetching the data from user
        name = request.POST.get('name')     
        email = request.POST.get('email')     
        contact = request.POST.get('contact')     
        password = request.POST.get('password')     
        repassword = request.POST.get('repassword')

        # Name Verification Code 
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
                
                # Mail Comfirmation
                send_mail(
                'Successfully Registered',
                'Hey Aman Saxena, You have been successfully registered in Adani World, Thank You',
                'aman16glbajaj@gmail.com',
                [email],
                fail_silently=False,
                )

                return render(request,'success.html')
            else:
                message = "Password is Improper, Should be between 8 - 20 Characters"
                return render(request,'error.html',{'error_text' : message})
            
        else:
            message = "Incorrect Password"
            return render(request,'error.html',{'error_text' : message})

    
    return render(request,'sign_up.html')

def login(request):
    if(request.method == 'POST'):
        # fatching the data from user
        email = request.POST.get('email') 
        password = request.POST.get('password') 

        # fetching the original data from database for validate
        user = SignUp.objects.values_list('name','email', 'password')
        for i in user:
            if(i[1] == email):
                # slicing the key from the user
                hash_pass = i[2][2:-1]
                clean_hash_pass = hash_pass.encode()  # encoding the key after the slicing
                decrypted_password = cipher_suite.decrypt(clean_hash_pass.decode()) #decrypting the password
                clean_decrypted_pass = (str(decrypted_password))[2:-1]

                # Checking the original password with user entered password
                if(password == clean_decrypted_pass):
                    message = "You Have successfully Logged Inn"
                    return render(request,'success.html',{'message' : message})
                
                else:
                    message = "Incorrect Password"
                    return render(request,'error.html',{'error_text' : message})

    return render(request,'login.html')

def test(request):
    return render(request, 'test.html')