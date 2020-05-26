import re

import mongoengine
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Class_Types import Customer
from .forms import CustomerForm


# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')


# Validates Customer form and displays content
def customerForm(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                cust = Customer(**form.cleaned_data)
                if valid_uniqueness(model=cust, form=form, request=request):
                    return HttpResponseRedirect('')
                    # return render(request, 'frontend/customerForm.html', {'form':form})
                else:
                    return render(request, 'frontend/customerForm.html', {'form': form})
            except:
                print(form.errors)
        else:
            return render(request, 'frontend/customerForm.html', {'form': form})
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
    return render(request, 'frontend/storeForm.html', {'cust': cust})


def workOrderForm(request):
    return render(request, 'frontend/workOrderForm.html')


def valid_uniqueness(model, form, request):
    try:
        model.save()
        messages.success(request, 'Successfully added.')
        return True

    except mongoengine.errors.NotUniqueError as e:
        for field in e.args:
            field_name = re.sub('.+?(?=index\:\ ){1}(index\:\ )|(\_.*)', '', field)
            form.add_error(field_name, 'Must be unique')
        return False
