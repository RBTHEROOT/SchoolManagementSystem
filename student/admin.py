from django.contrib import admin
from .models import Student, Fees
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['admissionNumber', 'name', 'std']
    class Meta:
        model = Student


class FeesAdmin(admin.ModelAdmin):
    list_display = ['admNo', 'previousDues', 'amount', 'amountPaid', 'dues']
    class Meta:
        model = Fees
admin.site.register(Student, StudentAdmin)
admin.site.register(Fees, FeesAdmin)