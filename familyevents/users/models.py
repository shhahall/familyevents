from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    dob=models.DateField()
    whatsapp_number=models.CharField(max_length=10)
    dp_image=models.ImageField(upload_to='media/dp/',null=True)
    role=models.IntegerField(default=0)
    work_points=models.IntegerField(default=0)