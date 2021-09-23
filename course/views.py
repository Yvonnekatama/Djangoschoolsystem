

from course.models import Course
from django.shortcuts import redirect, render
from .forms import  CourseForm
# Create your views here.
def view_course(request):
       if request.method=="POST":
           form=CourseForm(request.POST, request.FILES)
           if form.is_valid():
               form.save()
           else:
               print(form.errors)
       else:
            form=CourseForm()
       return render (request,"course.html",{"form":form})
def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses_list.html", {"courses": courses})
def edit_student(request,id):
    courses=Course.objects.get(id=id)
    if request.method=="POST":
        form=(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CourseForm(instance=Course)
        return render(request,"edit_course.html",{"form":form})
def student_profile(request,id):
    course=Course.objects.get(id=id)  
    return render(request,"course_profile.html",{"student":course})
def delete_student(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect('course_list')
  
