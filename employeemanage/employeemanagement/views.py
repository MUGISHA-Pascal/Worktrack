from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.views import View

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
    d1form2=department2.objects.all()
    d1form3=department3.objects.all()
    filter={
        "d1form":d1form,
        "d1form2":d1form2,
        "d1form3":d1form3
    }
    return render(request,"employees.html",filter)
def trainingrecords(request):
    return render(request,"trainingrecords.html")
def perfomance(request):
    return render(request,"perfomance.html")
def profile(request):
    return render(request,"profile.html")
def search(request):
    if request.method == "GET":
        employeename=request.GET.get("employeename")
        departmentname=request.GET.get("departmentname")
        if departmentname == "department 1":
            mdl=department1.objects.filter(employeename=employeename)
        elif departmentname == "department 2":
            mdl=department2.objects.filter(employeename=employeename)
        elif departmentname == "department 3":
            mdl=department3.objects.filter(employeename=employeename)
        else:
            return render(request,"search.html")
            
    return render(request,"search.html",{"mdl":mdl})
class manageemployees(View):
    def get(self,request):
        if request.method == "GET":
            employeename=request.GET.get("employeename")
            departmentname=request.GET.get("departmentname")
            if departmentname == "department 1":
                mdl=department1.objects.filter(employeename=employeename)
                mdl.delete()
            elif departmentname == "department 2":
                mdl=department2.objects.filter(employeename=employeename)
                mdl.delete()
            elif departmentname == "department 3":
                mdl=department3.objects.filter(employeename=employeename)
                mdl.delete()
            else:
                return render(request,"manageemployees.html")
        return render(request,"manageemployees.html")      
    def post(self,request): 
        if request.method == "POST":     
            employeename=request.POST["employeename"]
            departmentname=request.POST["departmentname"]
            if departmentname == "department 1":
                dp1=department1(employeename=employeename)
                dp1.save() 
            elif departmentname == "department 2":
                dp1=department2(employeename=employeename)
                dp1.save()   
            if departmentname == "department 3":
                dp1=department3(employeename=employeename)
                dp1.save()   
            else:
                return render(request,"manageemployees.html")
        return render(request,"manageemployees.html")
def changeprofile(request):
    if request.method == "POST":
        form=profileformi(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"profile.html",{"form":form})
    else:
        form=profileformi()
    return render(request,"profile.html",{"form":form})
    
        
                
                