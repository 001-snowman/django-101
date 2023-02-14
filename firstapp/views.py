from django.shortcuts import render,redirect
from . models import student

# Create your views here.
def index(request):
    return render(request, "index.html")

def add_student(request):
    return render(request, "add_student.html")

def display_students(request):
    if request.method=="POST":
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

def delete_student(request, id):
    student.objects.get(id=id).delete()
    return redirect("/display_students/")

def update_student(request, id):
    if request.method=="POST":
        a=student.objects.get(id=id)
        a.fname=request.POST['fname']
        a.lname=request.POST['lname']
        a.gender=request.POST['gender']
        a.country=request.POST['country']
        a.save()
        return redirect("/display_students/")

    else:
        data={
            'studentData':student.objects.get(id=id)
        }
        return render(request, "update_student.html", data)