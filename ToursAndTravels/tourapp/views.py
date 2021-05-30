
from django.shortcuts import render,redirect
from django.http import HttpResponse
import os
from tourapp.models import Car
from tourapp.form import CarForm
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'home.html')


def index(request):
	return render(request,'index.html')


    
@login_required
def addcar(request):
    obj=CarForm()
    if request.method=="POST":
         obj=CarForm(request.POST,request.FILES)
         if obj.is_valid():
             obj.save()
             return redirect('showcar')
         else:
             return HttpResponse("<h1>something is wrong</h1>")
    else:
        return render(request,'addcar.html',{'form':obj})



@login_required
def showcar(request):
    obj = Car.objects.all()
    return render (request,'showcar.html',{'form':obj})   



@login_required
def update_car(request,car_id):
    car_id = int(car_id)
    try:
        car_select = Car.objects.get(id=car_id)

    except Car.DoesNotExists:
        #return HttpResponse("Something is wrong")
        return redirect('index')

    else:
      Car_form = CarForm(request.POST or None ,instance = car_select)
      if Car_form.is_valid():
            old_img = ""
            if car_select.car_img:
                old_img =  car_select.car_img.path

                form =CarForm(request.POST,request.FILES,instance= car_select)
                if form.is_valid():
                    if os.path.exists(old_img):
                        os.remove(old_img)  
                        form.save() 
            return redirect('showcar')
      return render(request,'update.html',{'form':Car_form})   
      

@login_required
def delete(request,car_id):
    car_id = int(car_id)
    try:
        car_select =Car.objects.get(id = car_id)
        
    except Car.DoesNotExists:
        return redirect('index')

    
    car_select.delete()  
    return redirect('showcar')    


@login_required
def logout(request):
    return render(request,"logout.html") 




    
