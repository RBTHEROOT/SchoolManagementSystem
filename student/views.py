from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Admission, Std,FeeType,FeeStructure,FeeReceived
from django.core.urlresolvers import reverse_lazy
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class AdmissionCrate(CreateView):
    model = Admission
    fields = ['admissionNumber','studentName','std','gender','fatherName','mobileNumber','address','transport']
    success_url = reverse_lazy('student:index')

class AdmissionUpdate(UpdateView):
    model = Admission
    fields = ['admissionNumber','studentName','std','gender','fatherName','mobileNumber','address','transport']
    success_url = reverse_lazy('student:index')

class StdCreate(CreateView):
    model = Std
    fields = ['standard']
    success_url = reverse_lazy('student:index')

class StdUpadate(UpdateView):
    model = Std
    fields = ['standard']
    success_url = reverse_lazy('student:index')

class StdDelete(DeleteView):
    model = Std
    fields = ['standard']
    success_url = reverse_lazy('student:index')

class FeeTypeCreate(CreateView):
    model = FeeType
    fields = ['typeOfFee']
    success_url = reverse_lazy('student:index')


class FeeTypeUpdate(UpdateView):
    model = FeeType
    fields = ['typeOfFee']
    success_url = reverse_lazy('student:index')


class FeeStructureCreate(CreateView):
    model = FeeStructure
    fields = ['feeType','std','amount']
    success_url = reverse_lazy('student:index')


class FeeStructureUpdate(CreateView):
    model = FeeStructure
    fields = ['feeType','std','amount']
    success_url = reverse_lazy('student:index')

class FeeReceivedCreate(CreateView):
    model = FeeReceived
    fields = ['admNo','std','feeType', 'feeOfMonth', 'previousDues', 'amount','paidAmount','dues']
    success_url = reverse_lazy('student:index')

class FeeReceivedUpdate(UpdateView):
    model = FeeReceived
    fields = ['admNo','std','feeType', 'feeOfMonth', 'previousDues', 'amount','paidAmount','dues']
    success_url = reverse_lazy('student:index')


