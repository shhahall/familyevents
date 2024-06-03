from django.shortcuts import render,HttpResponse,redirect
from users.models import UserProfile
from django.contrib.auth.models import User
from . models import Works,BookedWorks
from services.models import Services
# Create your views here.
def work_menu(request):
    user=request.user
    if user.user_profile.role <= 1:
        return redirect('homepage')
    return render(request,'works/works_menu.html',{'user':user})
def create_work(request):
    user=request.user
    types=Services.objects.all()
    if request.method=='POST':
        name = request.POST.get('name')
        type = Services.objects.get(pk=request.POST.get('type'))
        date = request.POST.get('date')
        place = request.POST.get('place')
        from_time = request.POST.get('from_time')
        to_time = request.POST.get('to_time')
        slots=request.POST.get('slots')
        work=Works.objects.create(name=name,type=type,date=date,place=place,from_time=from_time,to_time=to_time,slots=slots)
        return redirect('works')
    return render(request,'works/create_work.html',{'types':types,'user':user})
def delete_work(request,pk):
    obj=Works.objects.get(pk=pk)
    obj.delete()
    return redirect("works")
    

def edit_work(request,pk):
    user=request.user
    obj=Works.objects.get(pk=pk)
    types=Services.objects.exclude(id=obj.type.id)
    if request.method=='POST':
        obj.name = request.POST.get('name')
        obj.type = Services.objects.get(pk=request.POST.get('type'))
        obj.date = request.POST.get('date')
        obj.description = request.POST.get('description')
        obj.place = request.POST.get('place')
        obj.from_time = request.POST.get('from_time')
        obj.to_time = request.POST.get('to_time') 
        obj.save()
        return redirect('works')
    return render(request,'works/edit_work.html',{'work':obj,'types':types,'user':user})

def list_works(request):
    user=request.user
    if user.user_profile.role <= 1:
        return redirect('homepage')
    works=Works.objects.all()
    is_authenticated = request.user.is_authenticated
    return render(request,'works/works.html',{'works':works,"is_authenticated":is_authenticated,'user':user})

def works_settings(request,pk):
    user=request.user
    return render(request,'works/work_settings.html',{'work_id':pk,'user':user})

def book_work(request,pk):
    work = Works.objects.get(pk=pk)
    user = request.user
    if work.slots > work.booked_slots:
        booked = BookedWorks.objects.create(user=user,work=work)
        work.booked_slots = work.booked_slots + 1
        work.save()
    else:
        return redirect('services')
    return redirect('works')

def list_bookings(request,work_id):
    pending_requests = BookedWorks.objects.filter(status=0,work_id=work_id)
    is_authenticated = request.user.is_authenticated
    user=request.user
    return render(request,'works/pending_requests.html',{'user':user,"pending_requests":pending_requests,"is_authenticated":is_authenticated})

def reject_booking(request,pk):
    booking=BookedWorks.objects.get(pk=pk)
    booking.delete()
    return redirect('bookingrequests',work_id=pk)

def accept_booking(request,pk):
    booking=BookedWorks.objects.get(pk=pk)
    booking.status = 1
    booking.save()
    return redirect('bookingrequests',work_id=pk)
def end_work(request,work_id):
    work = Works.objects.get(pk=work_id)
    employees = BookedWorks.objects.filter(work=work,status=1)
    for x in employees:
        x.user.user_profile.work_points += 20
        x.user.user_profile.save()
    work.delete()
    return redirect('works')
def work_history(request):
    user=request.user
    works=BookedWorks.objects.filter(user=user)
    return render(request,'works/work_history.html',{'user':user,'works':works})
def registered_employees(request,pk):
    user=request.user
    work = Works.objects.get(pk=pk)
    employees = BookedWorks.objects.filter(work=work,status=1)
    
    return render(request,'works/approved_requests.html',{'employees':employees,'user':user})