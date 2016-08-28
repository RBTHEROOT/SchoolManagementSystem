from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Admission(models.Model):
    admissionNumber = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=250, null=False)
    std = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    gender = models.CharField(max_length=10, null=False)
    fatherName = models.CharField(max_length=250, null=False)
    mobileNumber = models.IntegerField(null=False)
    address = models.CharField(max_length=250, null=False)
    transport = models.BooleanField()

    def __str__(self):
        return str(self.admissionNumber)
