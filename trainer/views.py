from django.shortcuts import redirect, render
from .models import Trainer
from .forms import TrainerRegistrationForm
def register_student(request):
    if request.method == "POST":
        form =TrainerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
         form = TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})
def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, "trainers_list.html", {"trainers": trainers})

def edit_student(request,id):
    trainers=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TrainerRegistrationForm(instance=Trainer)
        return render(request,"edit_trainer.html",{"form":form})
def trainer_profile(request,id):
    students=Trainer.objects.get(id=id)  
    return render(request,"trainer_profile.html",{"student":students})
def delete_trainer(request,id):
    students=Trainer.objects.get(id=id)
    students.delete()
    return redirect('trainers_list')
  




