from django.shortcuts import render,redirect
from . forms import Service_Create_Form
from . models import Services,Bookings
import os
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_service(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('dp')
        service=Services.objects.create(name=name,description=description,image=image)
        return redirect('services')
    return render(request,'services/create_service.html')

def list_services(request):
    service=Services.objects.all()
    is_authenticated = request.user.is_authenticated
    return render(request,'services/services.html',{'service':service,"is_authenticated":is_authenticated})

def edit_services(request,pk):
    service=Services.objects.get(pk=pk)
    if request.method == 'POST':
        service.name=request.POST.get('name')
        service.description=request.POST.get('description')
        image=request.FILES.get('dp')
        if image:
            service.image = image
        service.save()
        return redirect('services')
    return render(request,'services/edit_service.html',{'service':service})
        
def delete_services(request,pk):
    service=Services.objects.get(pk=pk)
    image_path = os.path.join(settings.MEDIA_ROOT, str(service.image))
    if os.path.exists(image_path):
        os.remove(image_path)
    service.delete()
    return redirect('services')
@login_required
def view_service(request,pk):
    service=Services.objects.get(pk=pk)
    if request.method == 'POST':
        date=request.POST.get('date')
        return redirect('createbooking',service_id=service.pk,date=date)
    return render(request,"services/services_view.html",{'service':service})

def view_service_2(request,pk):
    service=Services.objects.get(pk=pk)
    if request.method == 'POST':
        date=request.POST.get('date')
        return redirect('createbooking',service_id=service.pk,date=date)
    return render(request,"services/services_view_2.html",{'service':service})

def create_booking(request, service_id, date):
    user = request.user
    A="hey"
    service = Services.objects.get(pk=service_id)
    try:
        booking = Bookings.objects.create(service_name=service, user=user, date=date)
        return redirect('https://api.whatsapp.com/send?phone=919567706418&text='+ A)
    except Exception as e:
        return redirect('viewservice_2',pk=service_id)
