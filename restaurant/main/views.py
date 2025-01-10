from django.shortcuts import render,redirect
from .models import Contact,Category,Momo
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
