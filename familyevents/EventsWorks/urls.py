from django.urls import path
from . import views
urlpatterns=[
    path('creatework/',views.create_work,name='creatework'),
    path('editwork/<pk>',views.edit_work,name='editwork'),
    path('deletework/<pk>',views.delete_work,name='deletework'),
    path('bookwork/<pk>',views.book_work,name='bookwork'),
    path('worksmenu/',views.work_menu,name='workmenu'),
    path('works/',views.list_works,name='works'),
    path('bookingrequests/',views.list_bookings,name='bookingrequests'),
    path('editbooking/<pk>',views.accept_booking,name='acceptbooking'),
    path('rejectbooking/<pk>',views.reject_booking,name='rejectbooking'),
    path('approvedemployees/<pk>',views.registered_employees,name="approvedemployees")
]