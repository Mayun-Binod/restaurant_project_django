from django.shortcuts import render,redirect
from .models import Contact,Category,Momo
from datetime import datetime
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re
# Create your views here.
def index(request):
    cate=Category.objects.all()
    cateid=request.GET.get('category')
    if cateid:
        momo=Momo.objects.filter(category=cateid)
    else:
        momo=Momo.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        
        Contact.objects.create(name=name,email=email,message=message,phone=phone)
        return redirect('index')
    context={
        "cate":cate,
        "momo":momo,
        "cateid":cateid,
    }
    
    return render(request,'main/index.html',context)
def about(request):
    return render(request,'main/about.html')

def service(request):
    return render(request,'main/services.html')

def menu(request):
    return render(request,'main/menu.html')

def contact(request):
    return render(request,'main/contact.html')

def terms(request):
    return render(request,'main/terms.html')

def privacy(request):
    return render(request,'main/privacy.html')

def policy(request):
    return render(request,'main/policy.html')

def support(request):
    return render(request,'main/support.html')

    # ------------------------------auth part-----------------------------

def register(request):

    if request.method == 'POST':
        fname =request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password ==password1:
            try:
                validate_password(password)

                if User.objects.filter(username=username).exists():
                    messages.error(request,"username already exists!!")
                    return redirect('register')
                
                if User.objects.filter(email=email).exists():
                    messages.error(request,"email already exists!!")
                    return redirect('register')
                
                if not re.search(r'[A-Z]',password):
                    messages.error(request,"at least one upper case")
                    return redirect('register')
                
                if not re.search(r'\d',password):
                    messages.error(request,"at least one numeric case")
                    return redirect('register')
                                  
                User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password)
                messages.success(request,'register successfully !!')
                return redirect('log_in')
            except ValidationError as e:
                for error in  e.messages:
                    messages.error(request,error)
                return redirect("register")    
        else:
            messages.error(request,"your password and confirm password does not match")
            return redirect('register')

    return render(request, "auth/register.html")


def log_in(request):
    return render(request,'auth/login.html')
