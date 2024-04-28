from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from . import views
from . models import UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
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

        if username and email and password:
            try:
                # Create a new user object
                user = User.objects.create_user(username=username, email=email, password=password, first_name=firstName, last_name=lastName)
                # Create a UserProfile object
                userProfile = UserProfile.objects.create(user=user, dob=dob, whatsapp_number=whatsapp_number, dp_image=dp)
                # Optionally, you can directly call login() to log in the user after registration
                # login(request, user)
                # Redirect the user to a different page (e.g., login page) after registration
                # return redirect('login')
                return redirect('index_page')  # Redirect to the index page after successful registration
            except Exception as e:
                # Handle any exceptions (e.g., username or email already exists)
                print(f"Registration failed: {e}")
                # You can render a registration form again with an error message if needed
                return render(request, 'auth/register.html', {'error': 'Registration failed. Please try again.'})
        else:
            # Handle invalid form data (e.g., missing required fields)
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
            print('Invalid credentials')

    return render(request, 'auth/login.html')

@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html',{'user_profile':user_profile})

def logout_view(request):
    logout(request)
    return redirect(index_page)

