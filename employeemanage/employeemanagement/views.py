from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from .forms import *

def signupview(request):
    if request.method == "POST" :
        name=request.POST['name']
        password=request.POST['password']
        email=request.POST['email']
        code=request.POST['code']
        mdl=signupdatabase(name=name,password=password,email=email,code=code)
        if mdl is not None:
            mdl.save()
            return HttpResponseRedirect("login")
    return render(request,"signup.html")
def loginview(request):
    if request.method == "POST":
        name=request.POST["name"]
        password=request.POST['password']
        md=bool(any(signupdatabase.objects.filter(password=password)))
        if md :
            return HttpResponseRedirect("home")
        else : return render(request,"login.html")
    return render(request,"login.html")
def homeview(request):
    d1form=department1.objects.all()
    filter={
        "d1form":d1form
    }
    return render(request,"employees.html",filter)
def trainingrecords(request):
    return render(request,"trainingrecords.html")
def perfomance(request):
    return render(request,"perfomance.html")
def profile(request):
    return render(request,"profile.html")
def search(request):
    return render(request,"search.html")

        