from django.shortcuts import render,redirect
from . models import student

# Create your views here.
def index(request):
    return render(request,"index.html")

def create(request):
    return render(request,"create.html")

def submitform(request):
    f_name=request.POST['f_name']
    l_name=request.POST['l_name']
    city=request.POST['city']
    gender=request.POST['gender']
    country=request.POST['country']
    student.objects.create(f_name=f_name,l_name=l_name,city=city,gender=gender,country=country)
    return redirect("/display_students/")


def display_students(request):
    data={
        'studentsData':student.objects.all()

    }
    
    return render(request,"display_students.html",data)