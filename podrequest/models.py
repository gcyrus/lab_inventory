from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from auth_app.models import Engineer #This allows the use of the Engineer class

# Create your models here.


#Devices found in the lab
class Device(models.Model):
    serialnumber = models.CharField(max_length=12, primary_key=True)
    device_model = models.CharField(max_length=12)
    device_type = models.CharField(max_length=24)
    x0_ip = models.GenericIPAddressField(max_length=15, null=True)
    x1_ip = models.GenericIPAddressField(max_length=15)
    x1_subnetmask = models.GenericIPAddressField(max_length=15, null=True)
    x1_gateway = models.GenericIPAddressField(max_length=15, null=True)
    x3_ip = models.GenericIPAddressField(max_length=15, null=True)
    x3_subnetmask = models.GenericIPAddressField(max_length=15, null=True)
    x3_gateway = models.GenericIPAddressField(max_length=15, null=True)
    pod_rdpip = models.GenericIPAddressField(max_length=15)
    podnumber = models.IntegerField()
    firmware = models.CharField(max_length=12, null=True)
    available = models.BooleanField()

    #Gives quick information about the device object
    def __str__(self):
        return "Device: "+self.device_type+", Model: "+self.device_model+", Serialnumber: "+self.serialnumber


#Tracks the request history of a device
class RequestHistory(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    serialnumber = models.ForeignKey(Device, on_delete=models.CASCADE)
    date_requested = models.DateField()
    time_requested = models.TimeField()
    date_returned = models.DateField(null=True)
    time_returned = models.TimeField(null=True)

    def __str__(self):
        return "Engineer's email: "+self.email+", Serialnumber of device: "+self.serialnumber