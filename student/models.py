from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    admissionNumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, null=False)
    std = models.IntegerField(null=False)
    gender = models.CharField(max_length=10, null=False)
    fatherName = models.CharField(max_length=250, null=False)
    mobileNumber = models.IntegerField(null=False)
    address = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.name + '-'+ str(self.admissionNumber)
