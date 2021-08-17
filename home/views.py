from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login

from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        desc =request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Successfully Updated !!!')
    return render(request,'contact.html')
    
def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
        # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def signup(request):
     if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # check if user has entered correct credentials
        user = User.objects.create_user(username=username, email=email,password=password)
        user.save()
        user = authenticate(username=username, email=email,password=password)
        if user is not None:
        # A backend authenticated the credentials
            authenticate(username=request.POST['username'],email=request.POST['email'], password=request.POST['password'])
            return redirect("/login")
        else:
        # No backend authenticated the credentials
            return render(request,'signup.html')
     return render(request,'signup.html')
    
def logoutUser(request):
    logout(request)
    return redirect("/login")
    