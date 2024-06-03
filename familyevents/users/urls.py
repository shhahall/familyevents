from django.urls import path
from . import views
urlpatterns=[
   path('',views.index_page,name='homepage'),
   path('alert/<data>/',views.alert,name='alert'),
   path('login/',views.login_page,name='loginpage'),
   path('register/',views.register_page,name='registerpage'),
   path('logout/',views.logout_view,name='logout'),
   path('profile/',views.view_profile,name='viewprofile'),
   path('editprofile/',views.edit_profile,name='editprofile'),
   path('editprofileimage/',views.edit_profile_image,name='editprofileimage'),
]