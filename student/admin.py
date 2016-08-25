from django.contrib import admin
from .models import Admission,FeeType,FeePaid,FeeStructure
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['admissionNumber', 'name', 'std']
    class Meta:
        model = Admission

class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ['std', 'feeType', 'amount']
    class Meta:
        model = FeeStructure

class FeePaidAdmin(admin.ModelAdmin):
    list_display = ['receiptNo', 'admissionNumber', 'amount', 'paidAmount', 'dues', 'date']
    class Meta:
        model = FeePaid



admin.site.register(Admission, StudentAdmin)
admin.site.register(FeeType)
admin.site.register(FeePaid, FeePaidAdmin)
admin.site.register(FeeStructure, FeeStructureAdmin)