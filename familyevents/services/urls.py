from django.urls import path
from . import views
urlpatterns=[
  path('createservice/',views.create_service,name='createservice'),
  path('deleteservice/<pk>',views.delete_services,name='deleteservice'),
  path('services/',views.list_services,name='services'),
]