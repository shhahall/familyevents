from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='media/',null=True)

class Bookings(models.Model):
    service_name=models.ForeignKey(Services,on_delete=models.SET_NULL,related_name='service_name',null=True)
    date=models.DateField(unique=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='booked_user',null=True)