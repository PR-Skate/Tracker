from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Class_Types import *
from .forms import CustomerForm
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def customerForm(request):
    if request.method =='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                cust = Customer(**form.cleaned_data)
                exists = Customer.objects.filter(customerName=cust.customerName)
                if not exists:
                    cust.save()
                    messages.success(request, 'Successfully added.')

                    return HttpResponseRedirect('')
                    #return render(request, 'frontend/customerForm.html', {'form':form})
                else:
                    form.add_error('customerName', 'Must be unique')
                    return render(request, 'frontend/customerForm.html', {'form':form})
            except:
                print(form.errors)
        else:
            return render(request, 'frontend/customerForm.html', {'form':form})
    else:
        pass
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


