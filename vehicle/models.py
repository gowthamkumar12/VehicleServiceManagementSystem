from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    categoryname = models.CharField(max_length=100)
    def __str__(self):
        return self.categoryname

class EnquiryType(models.Model):
    enqtypename = models.CharField(max_length=100)
    def __str__(self):
        return self.enqtypename


class Enquiry(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    enqno = models.CharField(max_length=15)
    enqtype = models.ForeignKey(EnquiryType, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    enqdate = models.DateField()
    adminresponse = models.CharField(max_length=500,null=True)
    adminstatus = models.CharField(max_length=50,null=True)
    adminremarkdate = models.DateField(null=True)
    def __str__(self):
        return self.enqno


class Mechanic(models.Model):
    fullname = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=15)
    emailid = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    def __str__(self):
        return self.fullname


class ServiceRequest(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    serviceno = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vehiclename = models.CharField(max_length=100)
    vehiclemodel = models.CharField(max_length=30)
    vehiclebrand = models.CharField(max_length=50)
    vehicleregno = models.CharField(max_length=15)
    servicedate = models.DateField()
    servicetime = models.TimeField()
    deltype = models.CharField(max_length=50)
    pickupaddr = models.CharField(max_length=300)
    servicereqdate = models.DateField(null=True)
    serviceby = models.ForeignKey(Mechanic, on_delete=models.CASCADE,null=True)
    servicecharge = models.CharField(max_length=50,null=True)
    partscharge = models.CharField(max_length=50,null=True)
    othercharge = models.CharField(max_length=50,null=True)
    adminremark = models.CharField(max_length=500,null=True)
    adminstatus = models.CharField(max_length=100,null=True)
    adminremarkdate = models.DateField(null=True)
    def __str__(self):
        return self.serviceno


