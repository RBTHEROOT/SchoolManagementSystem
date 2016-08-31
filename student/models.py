from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Std(models.Model):
    standard = models.CharField(max_length=3)

    def __str__(self):
        return self.standard

class FeeType(models.Model):
    typeOfFee = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.typeOfFee


class Month(models.Model):
    monthName = models.CharField(max_length=15)
    def __str__(self):
        return self.monthName

class FeeStructure(models.Model):

    class Meta:
        unique_together = (('feeType', 'std'), )
    feeType = models.ForeignKey(FeeType)
    std = models.ForeignKey(Std)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.std)+ ' - ' + self.feeType.typeOfFee

class Admission(models.Model):
    admissionNumber = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=250, null=False)
    std = models.ForeignKey(Std)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    gender = models.CharField(max_length=10, null=False)
    fatherName = models.CharField(max_length=250, null=False)
    mobileNumber = models.IntegerField(null=False)
    address = models.CharField(max_length=250, null=False)
    transport = models.BooleanField()

    def __str__(self):
        return str(self.admissionNumber)


class FeeReceived(models.Model):
    admNo = models.ForeignKey(Admission, related_name='+')
    std = models.CharField(max_length=3)
    date = models.DateField(auto_now_add=True)
    feeType = models.ManyToManyField(FeeType)
    feeOfMonth = models.ManyToManyField(Month)
    previousDues = models.IntegerField()
    amount = models.IntegerField()
    paidAmount = models.IntegerField()
    dues = models.IntegerField()

    def __str__(self):
        return str(self.admNo)
