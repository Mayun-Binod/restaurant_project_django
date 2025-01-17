from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User

# for password validation
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

import re

#for authentication[login ko laagi]
from django.contrib.auth import authenticate,login,logout

#decorator[without login when we click on home,about, it redirect to login page]
from django.contrib.auth.decorators import login_required

from .models import Contact,Category,Momo
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def index(request):
    cate = Category.objects.all()

    cateid = request.GET.get('category')
    if cateid:
        # data = Momo.objects.filter(category=cateid)
        momo = Momo.objects.filter(category=cateid)
    else:

        # data= Momo.objects.all()
        momo= Momo.objects.all()
      

    #context dictionary
    context = {
        "cate":cate,
        # "data":data,
        "momo":momo,
        "cateid":cateid,
        "date":datetime.now
    }

    return render(request, "main/index.html", context)

@login_required(login_url="log_in")
def about(request):
    return render(request, "main/about.html")

@login_required(login_url="log_in")
def menu(request):
    return render(request, "main/menu.html")

@login_required(login_url="log_in")
def services(request):
    return render(request, "main/services.html")


def contact(request):
    if request.method == "POST":
        data = request.POST         #data is recived in the form dictionary

        # print("===========================================")
        # print(data["fullName"])
        #store each form data in a variable
        # # fn = data.get("fullName")
        # fn = data["fullName"]
        # email = data["email"]
        # phone_no = data["phoneNumber"]
        # message = data["mssg"]

         # fn = data.get("fullName")
        fn = data.get("name")
        email = data.get("email")
        phone_no = data.get("phone")
        message = data.get("msg")


        contact = Contact(name=fn,email=email,phone_number=phone_no,message=message)
        contact.save()
        # return redirect('contact')
        return render(request, "main/contact.html")


    return render(request, "main/contact.html")


def termsAndCondition(request):
    return render(request, "main/terms_and_condition.html")

def privacy(request):
    return render(request, "main/privacy.html")

def policy(request):
    return render(request, "main/policy.html")

def support(request):
    return render(request, "main/support.html")


def register(request):
    if request.method == "POST":
        fn = request.POST["first_name"]
        ln = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        if password == password1:
            try:
                validate_password(password)

                if User.objects.filter(username=username).exists():
                    messages.error(request, "username already exists ..!!")
                    return redirect('register')  
        
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email already exists ..!!")
                    return redirect('register') 

                
                #for more validation By ourself
                if not re.search(r'[A-Z]',password):
                    messages.error(request, "password contain at least one Upper case")
                    return redirect('register') 
                
                if not re.search(r'\d',password):
                    messages.error(request, "password contain at least one numeric case")
                    return redirect('register') 

                User.objects.create_user(first_name=fn,last_name=ln,username=username,email=email,password=password)
                messages.success(request, "register successfully ..!!")
                return redirect('login')
        
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request,error)
                return redirect('register')
            
        else:
            messages.error(request, "your password and confirm password doesnot match")
            return redirect('register')

    return render(request, "auth/register.html")

"""
def log_in(request):
    if request.method == "POST":
        un = request.POST["username"]
        password = request.POST["password"]

        if not User.objects.filter(username=un).exists():
            messages.error(request,"username is not registered yet!!")
            return redirect('log_in')
        
        user = authenticate(username=un,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,"invalid password...!!")
            return redirect('log_in')

    return render(request, "auth/login.html")

"""

def log_in(request):
    if request.method == "POST":
        un = request.POST["username"]
        password = request.POST["password"]
        # remember_me = request.POST["remember_me"]
        remember_me = request.POST.get("remember_me")

        if not User.objects.filter(username=un).exists():
            messages.error(request,"username is not registered yet!!")
            return redirect('log_in')
        
        user = authenticate(username=un,password=password)
        
        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(1200000)     #add session
            else:
                request.session.set_expiry(0)        #session destroy(kill)
            
            #receive form data next
            # next = request.POST.get('next',"")
            next = request.POST.get("next","")

            # return redirect('index')
            return redirect(next if next else 'index')
        else:
            messages.error(request,"invalid password...!!")
            return redirect('log_in')

    # next = request.GET.get('next,"")
    next = request.GET.get("next","")

    return render(request, "auth/login.html", {"next":next})


def log_out(request):
    logout(request)
    return redirect('log_in')

@login_required(login_url='log_in')
def change_password(request):
    form=PasswordChangeForm(user=request.user)
    if request.method=="POST":
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request,'auth/change_password.html',{"form":form})


