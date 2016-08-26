from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Admission(models.Model):
    admissionNumber = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False)
    std = models.IntegerField(null=False)
    gender = models.CharField(max_length=10, null=False)
    fatherName = models.CharField(max_length=250, null=False)
    mobileNumber = models.IntegerField(null=False)
    address = models.CharField(max_length=250, null=False)
    transport = models.BooleanField()

    def __str__(self):
        return str(self.admissionNumber)


class FeeType(models.Model):
    feeType = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.feeType

class FeeStructure(models.Model):
    std = models.IntegerField()
    feeType = models.ForeignKey(FeeType)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.std)

class FeePaid(models.Model):
    receiptNo = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    admissionNumber = models.ForeignKey(Admission)
    feeOfMonth = models.CharField(max_length=12)
    previousDues = models.IntegerField(default=0)
    amount = models.IntegerField()
    paidAmount = models.IntegerField()
    dues = models.IntegerField()

    def __str__(self):
        return str(self.admissionNumber)

class StudentRecord(models.Model):
    admissionNumber = models.ForeignKey(FeePaid.admissionNumber, on_delete=models.CASCADE)
    name = models.ForeignKey(Admission.std)
    std = models.ForeignKey(Admission.std)
    feePaidOfMonth = models.ForeignKey(FeePaid.feeOfMonth)
    amountPaid = models.ForeignKey(FeePaid.previousDues)
    duesAmount = models.ForeignKey(FeePaid.dues)

    def __str__(self):
        return str(self.admissionNumber)








