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
    modl=trainingdb.objects.all()
    form=imagedb.objects.filter().last()
    filt={
        "form":form,
        "modl":modl
    }
    return render(request,"trainingrecords.html",{"filt":filt})
def perfomance(request):
    modl=perfomancedb.objects.all()
    form=imagedb.objects.filter().last()
    filt={
        "modl":modl,
        "form":form
    }
    return render(request,"perfomance.html",{"filt":filt})
def profile(request):
    form=imagedb.objects.filter().last()
    filt={
        "form":form
    }
    return render(request,"profile.html",{"filt":filt})
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
class manageperfomance(View):
    def get(self,request):
        if request.method == "GET":
            perfomance=request.GET.get("perfomance")
            perfomancedate=request.GET.get("perfomancedate")
            modl=perfomancedb.objects.filter(perfomance=perfomance,perfomancedate=perfomancedate)
            if modl is not None:
                modl.delete()
        return render(request,"manageperfomance.html")
    def post(self,request): 
        if request.method == "POST":     
            perfomance=request.POST["perfomance"]
            perfomancedate=request.POST["perfomancedate"]
            modl=perfomancedb(perfomance=perfomance,perfomancedate=perfomancedate)
            if modl is not None:
                modl.save()
        return render(request,"manageperfomance.html")
class managetraining(View):
    def get(self,request):
        if request.method == "GET":
            training=request.GET.get("training")
            trainingdate=request.GET.get("trainingdate")
            modl=trainingdb.objects.filter(training=training,trainingdate=trainingdate)
            if modl is not None:
                modl.delete()
        return render(request,"managetraining.html")
    def post(self,request): 
        if request.method == "POST":     
            training=request.POST["training"]
            trainingdate=request.POST["trainingdate"]
            modl=trainingdb(training=training,trainingdate=trainingdate)
            if modl is not None:
                modl.save()
        return render(request,"managetraining.html")
def changeprofile(request):
    if request.method == "POST":
        form=imageform(request.POST,request.FILES)
        if form.is_valid:
            form.save()
    else:
        form=imageform()
    return render(request,"changeprofile.html",{"form":form})

    
        
                
                