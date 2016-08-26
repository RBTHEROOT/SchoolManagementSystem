from django.contrib import admin
from .models import Admission,FeeType,FeePaid,FeeStructure,StudentRecord
# Register your models here.


class AdmissionAdmin(admin.ModelAdmin):
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
#
# class StudentRecordAdmin(admin.ModelAdmin):
#     list_display = ['admissionNumber', 'name', 'std', 'feePaidOfMonth', 'amountPaid', 'duesAmount']
#     class Meta:
#         model = StudentRecord

admin.site.register(Admission, AdmissionAdmin)
admin.site.register(FeeType)
admin.site.register(FeePaid, FeePaidAdmin)
admin.site.register(FeeStructure, FeeStructureAdmin)
admin.site.register(StudentRecord)