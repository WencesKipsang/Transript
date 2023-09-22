from django.shortcuts import render,redirect,HttpResponse
from . import forms
from django.contrib import messages
from . import models
# Create your views here.

def admin_dashboard(request):
    return render (request,'admin_home.html')

def admin_home(request):
    if request.method=='POST':
        form=forms.AddStudent(request.POST)
        if form.is_valid():
            me=form.save()             
            if me:
                 messages.success(request,'Student'+form.student_name+'is Saved Successfully..!') 
                 return redirect('home')
            else:
                 messages.success(request,'Student Not Saved ..!') 
                 return redirect('home')
        else:
            messages.success(request,'Student Not Saved ..! Please Fill all the required fields properly ..!') 
            return redirect('home')
    else:
        form= forms.AddStudent()
    
    studee=models.Student.objects.all()    
    return render(request, 'admin_home.html',{'form':form,'students':studee})

def add_unit(request):
    if request.method=='POST':
        form=forms.AddUnit(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=forms.AddUnit()
    return render(request, 'add_unit.html',{'form':form}) 

def add_course(request):
    if request.method=='POST':
        form=forms.AddCourse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=forms.AddCourse()
    return render(request, 'add_courses.html')

def chart(request):
    return render(request, 'chart.html')
