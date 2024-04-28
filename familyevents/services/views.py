from django.shortcuts import render,redirect
from . forms import Service_Create_Form
from . models import Services
import os
from django.conf import settings
# Create your views here.
def create_service(request):
    if request.method == 'POST':
        form=Service_Create_Form(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('homepage')
    else:
        form=Service_Create_Form()
    return render(request,'services/createservice.html',{'form':form})

def list_services(request):
    service=Services.objects.all()
    return render(request,'services/services.html',{'service':service})

def delete_services(request,pk):
    service=Services.objects.get(pk=pk)
    image_path = os.path.join(settings.MEDIA_ROOT, str(service.image))
    if os.path.exists(image_path):
        os.remove(image_path)
    service.delete()
    return redirect('services')

        