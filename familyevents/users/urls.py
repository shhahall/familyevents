from django.urls import path
from . import views
urlpatterns=[
   path('',views.index_page,name='homepage'),
   path('login/',views.login_page,name='loginpage'),
   path('register/',views.register_page,name='registerpage'),
   path('logout/',views.logout_view,name='logout'),
   path('profile/',views.view_profile,name='viewprofile')
]