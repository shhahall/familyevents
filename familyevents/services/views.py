from django.shortcuts import render,redirect
from . forms import Service_Create_Form
from . models import Services,Bookings
import os
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

# Create your views here.
def create_service(request):
    if request.method == 'POST':
        form=Service_Create_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form=Service_Create_Form()
    return render(request,'services/createservice.html',{'form':form})

def list_services(request):
    service=Services.objects.all()
    is_authenticated = request.user.is_authenticated
    return render(request,'services/services.html',{'service':service,"is_authenticated":is_authenticated})

def edit_services(request,pk):
    service=Services.objects.get(pk=pk)
    if request.method == 'POST':
        form=Service_Create_Form(request.POST,request.FILES,instance=service)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form=Service_Create_Form(instance=service)
    return render(request,'services/createservice.html',{'form':form})
        
def delete_services(request,pk):
    service=Services.objects.get(pk=pk)
    image_path = os.path.join(settings.MEDIA_ROOT, str(service.image))
    if os.path.exists(image_path):
        os.remove(image_path)
    service.delete()
    return redirect('services')

def view_service(request,pk):
    service=Services.objects.get(pk=pk)
    if request.method == 'POST':
        date=request.POST.get('date')
        return redirect('createbooking',service_id=service.pk,date=date)
    return render(request,"services/view_service.html",{'service':service})


def create_booking(request, service_id, date):
    user = request.user
    service = Services.objects.get(pk=service_id)
    try:
        booking = Bookings.objects.create(service_name=service, user=user, date=date)
        return redirect('homepage')
    except Exception as e:
        return redirect('alert',data='Not Available for this Date')