from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from . import views
from . models import UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
def alert(request,data):
    return render(request,'alert.html',{"data":data})

def index_page(request):
    user=request.user
    is_authenticated = request.user.is_authenticated
    
    return render(request,'index.html', {'user': user, 'is_authenticated': is_authenticated})

def register_page(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        whatsapp_number = request.POST.get('whatsapp_number')
        dp = request.FILES.get('dp')
        if not dp:
            dp = 'media/dp/default.png'
        if username and email and password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=firstName, last_name=lastName)
                userProfile = UserProfile.objects.create(user=user, dob=dob, whatsapp_number=whatsapp_number, dp_image=dp)
                return redirect('index_page')  
            except Exception as e:
                print(f"Registration failed: {e}")
                return render(request, 'auth/register.html', {'error': 'Registration failed. Please try again.'})
        else:
            return render(request, 'auth/register.html', {'error': 'Invalid form data. Please provide all required fields.'})
    return render(request, 'auth/register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('homepage')
            # Optionally, you can redirect the user to a different page after successful login
        else:
            # Authentication failed
            return redirect('alert',data="Invalid Credentials")

    return render(request, 'auth/login.html')

@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html',{'user_profile':user_profile})

def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method=='POST':
        user_profile.user.username=request.POST.get('username')
        user_profile.user.first_name=request.POST.get('first_name')
        user_profile.user.last_name=request.POST.get('last_name')
        user_profile.user.email=request.POST.get('email')
        user_profile.whatsapp_number=request.POST.get('whatsapp_number')
        user_profile.save()
        user_profile.user.save()
        return redirect('viewprofile')
    return render(request, 'profile_edit.html',{'user_profile':user_profile})

def edit_profile_image(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method=='POST':
        image=request.FILES.get('dp')
        if image:
            user_profile.dp_image=image
            user_profile.save()
            return redirect('editprofile')
    return render(request,'profile_edit_image.html',{'user_profile':user_profile})

def logout_view(request):
    logout(request)
    return redirect(index_page)
