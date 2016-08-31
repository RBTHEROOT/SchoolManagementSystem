from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Admission, Std,FeeType,FeeStructure,FeeReceived,Month
# Create your views here.


class AdmissionCrate(CreateView):
    model = Admission
    fields = ['admissionNumber','studentName','std','gender','fatherName','mobileNumber','address','transport']

class AdmissionUpdate(UpdateView):
    model = Admission
    fields = ['admissionNumber','studentName','std','gender','fatherName','mobileNumber','address','transport']


class StdCreate(CreateView):
    model = Std
    fields = ['standard']


class StdUpadate(UpdateView):
    model = Std
    fields = ['standard']

class StdDelete(DeleteView):
    model = Std
    fields = ['standard']

class FeeTypeCreate(CreateView):
    model = FeeType
    fields = ['typeOfFee']


class FeeTypeUpdate(UpdateView):
    model = FeeType
    fields = ['typeOfFee']


class FeeStructureCreate(CreateView):
    model = FeeStructure
    fields = ['feeType','std','amount']


class FeeStructureUpdate(CreateView):
    model = FeeStructure
    fields = ['feeType','std','amount']

class FeeReceivedCreate(CreateView):
    model = FeeReceived
    fields = ['admNo','std','feeType', 'feeOfMonth', 'previousDues', 'amount','paidAmount','dues']

class FeeReceivedUpdate(UpdateView):
    model = FeeReceived
    fields = ['admNo','std','feeType', 'feeOfMonth', 'previousDues', 'amount','paidAmount','dues']


