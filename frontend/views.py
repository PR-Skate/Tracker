from django.shortcuts import render
from Class_Types import *

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def customerForm(request):
    return render(request, 'frontend/customerForm.html')

def employeeForm(request):
    return render(request, 'frontend/employeeForm.html')

def prepWorkForm(request):
    return render(request, 'frontend/prepWorkForm.html')

def sowForm(request):
    return render(request, 'frontend/sowForm.html')

def storeForm(request):
    cust = Customer.objects.all()
    return render(request, 'frontend/storeForm.html', {'cust':cust})

def workOrderForm(request):
    return render(request, 'frontend/workOrderForm.html')


