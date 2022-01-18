from turtle import title
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import *
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from course import models



def home(request):
    data=teacher.objects.all().order_by('pk')[:3]
    return render(request, 'course/home.html', {'datas':data})

def educator(request):
    
    return render(request,'course/creator_form.html')
    """if request.method == "POST":
        form=teacher_form(request.POST, request.FILES)
        form.instance.name = request.user

        if form.is_valid():
            form.save()
            messages.success(request, 'YAour Form has been submitted. It will be reviewed and decision will be communicated shortly')
            form=teacher_form()
            return render(request,'course/creator_form.html', {'form': form})

        else:
            print ("else entered")
    else:
        form=teacher_form()
        return render(request,'course/creator_form.html', {'form': form})"""

def edu_submit(request):
    if request.method =="POST":
        first=request.POST.get('fn')
        last=request.POST.get("ln")
        name=first+" "+ last
        email=request.POST.get('email')
        city=request.POST.get("city")
        dob=request.POST.get("dob")
        state=request.POST.get('state')
        about=request.POST.get("about")
        application=teacher_app(username=request.user , name=name,email=email, city=city, state=state, about=about, dob=dob, join_date=datetime.today())
        application.save()
        a=userDetail.objects.filter(username=request.user)
        i=0
        for x in a:
            i+=1
        if (i==0):
            usr_detail=userDetail(username=request.user , name=name,email=email, city=city, state=state, about=about, dob=dob, join_date=datetime.today())
            usr_detail.save()
        messages.success(request, 'Your application has been submitted.')
        return redirect("")

def usr_detail(request):
    a=userDetail.objects.filter(username=request.user)
    i=0
    for x in a:
        i+=1

    if (i==0):

    
        if request.method =="POST":
            first=request.POST.get('fn')
            last=request.POST.get("ln")
            name=first+" "+ last
            email=request.POST.get('email')
            city=request.POST.get("city")
            dob=request.POST.get("dob")
            state=request.POST.get('state')
            about=request.POST.get("about")
            usr_detail=userDetail(username=request.user , name=name,email=email, city=city, state=state, about=about, dob=dob, join_date=datetime.today())
            usr_detail.save()
            messages.success(request, 'Your details have been updated.')
        
            return redirect("/details/")

        return render(request, "course/details.html")

    else:
        data=userCourse.objects.filter(un=request.user)
        instr=teacher.objects.filter(name=request.user)
        data2=models.course.objects.filter(instructor__name__username=request.user)
        
        return render(request, "course/profile.html", {'datas':a, 'courses': data, 'creations':data2})

def add_course(request):
    if request.method == "POST":
        form=courseForm(request.POST, request.FILES)
        form.instance.instructor = teacher.objects.filter(name=request.user)[0]

        if form.is_valid():
            form.save()
            messages.success(request, 'Your course has been created ')
            form=courseForm()
            return render(request,'course/course_add.html', {'form': form})

        else:
            print ("else entered")
    else:
        form=courseForm()
        return render(request,'course/course_add.html', {'form': form})
    
def coursePage(request):
    datas=course.objects.all().order_by('-pk')
    return render(request, 'course/course.html', {'datas':datas})

def courseView(request):
    nm=1
    if request.method=="GET":
        nm=request.GET.get('s')
    datas=course.objects.get(pk=nm)
    return render(request, 'course/course_page.html', {'datas':datas})

def enroll(request):
    un=request.user
    id=request.GET.get('s')
    nm=request.GET.get('nm')
    s=userCourse(un=un.username, id=id, nm=nm)
    s.save()
    messages.success(request, "You have been enrolled to the course")
    return redirect("/course/?s={}".format(id))

def certificate(request):
    if (request.method=='GET'):
        name=request.user.first_name+ " "+ request.user.last_name
        course=request.GET.get('s')
        d=models.course.objects.filter(pk=course)[0]
        certi=models.certificate(course=d.title, name=name)
        certi.save()
        messages.success(request, "your certificate has been generated")
        return redirect("/course/?s={}".format(course))

def certification(request):
    datas=models.certificate.objects.filter(name=request.user.first_name+ ' '+request.user.last_name)
    return render(request, 'course/certificates.html', {'datas':datas})

def view_certificate(request):
    certi=request.GET.get('s')
    data=models.certificate.objects.filter(pk=certi)
    return render(request, 'course/certificatepage.html', {'datas':data})

def search(request):
    nm='sd'
    if request.method=="GET":
        nm=request.GET.get("search")

    datas1=course.objects.filter(title__icontains=nm)
    datas2=course.objects.filter(instructor__name__first_name__icontains=nm)
    datas8=course.objects.filter(instructor__name__last_name__icontains=nm)
    datas3=course.objects.filter(description__icontains=nm)
    datas4=course.objects.filter(areas__area__icontains=nm)
    datas5=datas1.union(datas2)
    datas6=datas3.union(datas4)
    datas7=datas5.union(datas6)
    datas9=datas7.union(datas8)
    return render(request,'course/search.html', {'datas':datas9})