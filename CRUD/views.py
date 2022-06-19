from django.shortcuts import redirect, render

# Create your views here
from .models import Student


def home(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        data=Student(name=name,email=email,password=password)
        data.save()
    
    d=Student.objects.all()
    return render(request,'add_show.html',{'data':d})

def delete_data(request,id):
    data=Student(pk=id)
    data.delete()
    return redirect('/')


def update_data(request,id):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        data=Student(pk=id,name=name,email=email,password=password)
        data.save()
        return redirect('/')

    data=Student.objects.get(pk=id)

    return render(request,'update.html',{'data':data})








