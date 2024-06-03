from django.db import models
from services.models import Services
from django.contrib.auth.models import User

# Create your models here.
class Works(models.Model):
    name=models.CharField(max_length=200)
    type=models.ForeignKey(Services,on_delete=models.SET_NULL,related_name='service_type',null=True)
    date=models.DateField()
    place=models.CharField(max_length=500)
    from_time=models.TimeField()
    to_time=models.TimeField()
    slots=models.IntegerField()

class BookedWorks(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='booked_workers',null=True)
    work=models.ForeignKey(Works,on_delete=models.SET_NULL,related_name='booked_works',null=True)
    status = models.IntegerField(default=0)

