from django.contrib import admin
from .models import Admission,FeeType,FeeStructure
# Register your models here.

admin.site.register(Admission)
admin.site.register(FeeType)
admin.site.register(FeeStructure)