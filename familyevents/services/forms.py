from django.forms import ModelForm
from . models import Services, Bookings
class Service_Create_Form(ModelForm):
    class Meta:
        model=Services
        fields='__all__'