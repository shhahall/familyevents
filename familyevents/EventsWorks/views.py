from django.shortcuts import render,HttpResponse,redirect
from users.models import UserProfile
from django.contrib.auth.models import User
from . models import Works,BookedWorks
from services.models import Services
# Create your views here.
def work_menu(request):
    return render(request,'works/works_menu.html')
def create_work(request):
    types=Services.objects.all()
    if request.method=='POST':
        name = request.POST.get('name')
        type = Services.objects.get(pk=request.POST.get('type'))
        date = request.POST.get('date')
        description = request.POST.get('description')
        place = request.POST.get('place')
        from_time = request.POST.get('from_time')
        to_time = request.POST.get('to_time')
        work=Works.objects.create(name=name,type=type,date=date,description=description,place=place,from_time=from_time,to_time=to_time)
        return HttpResponse('BOOKED')
        return redirect('works')
    return render(request,'works/create_work.html',{'types':types})
def delete_work(request,pk):
    obj=Works.objects.get(pk=pk)
    obj.delete()
    return redirect("works")
    

def edit_work(request,pk):
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
    return render(request,'works/edit_work.html',{'work':obj,'types':types})

def list_works(request):
    works=Works.objects.all()
    is_authenticated = request.user.is_authenticated
    return render(request,'works/works.html',{'works':works,"is_authenticated":is_authenticated})

def book_work(request,pk):
    work = Works.objects.get(pk=pk)
    user = request.user
    booked = BookedWorks.objects.create(user=user,work=work)
    return redirect('works')

def list_bookings(request):
    works = BookedWorks.objects.exclude(status=1)
    is_authenticated = request.user.is_authenticated
    return render(request,'works/pending_works_requests.html',{"works":works,"is_authenticated":is_authenticated})

def reject_booking(request,pk):
    booking=BookedWorks.objects.get(pk=pk)
    booking.delete()
    return redirect('bookingrequests')

def accept_booking(request,pk):
    booking=BookedWorks.objects.get(pk=pk)
    booking.status = 1
    booking.save()
    return redirect('bookingrequests')

def registered_employees(request,pk):
    work = Works.objects.get(pk=pk)
    employees = BookedWorks.objects.filter(work=work,status=1)
    
    return render(request,'works/employees_registered.html',{'employees':employees})