from django.urls import path
from . import views
urlpatterns=[
  path('createservice/',views.create_service,name='createservice'),
  path('deleteservice/<pk>',views.delete_services,name='deleteservice'),
  path('editservice/<pk>',views.edit_services,name='editservice'),
  path('services/',views.list_services,name='services'),
  path('viewservice/<pk>',views.view_service,name='viewservice'),
  path('create_booking/<int:service_id>/<str:date>/',views.create_booking,name='createbooking')
]