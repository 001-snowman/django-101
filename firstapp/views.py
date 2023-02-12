from django.shortcuts import render,redirect
from . models import student

# Create your views here.
def index(request):
    return render(request, "index.html")

def add_student(request):
    return render(request, "add_student.html")

def display_students(request):
    if request.method=="post":
        fname=request.POST['fname']
        lname=request.POST['lname']
        gender=request.POST['gender']
        country=request.POST['country']
        student.objects.create(fname=fname, lname=lname, gender=gender, country=country)
        return redirect("/display_students/")
    else:
        data={
            'studentData':student.objects.all()
        }
        return render(request, "display_students.html", data)