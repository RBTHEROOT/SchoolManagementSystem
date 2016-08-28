from django.contrib import admin
from .models import Admission,FeeType,FeeStructure,FeeReceived,Month,Std
# Register your models here.

admin.site.register(Admission)
admin.site.register(FeeType)
admin.site.register(FeeStructure)
admin.site.register(FeeReceived)
admin.site.register(Month)
admin.site.register(Std)