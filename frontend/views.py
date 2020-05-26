import re

import mongoengine
from django.contrib import messages
from django.http import HttpResponseRedirect
from Class_Types import Employee, Address, Name
from .forms import EmployeeForm
from mongoengine.errors import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Class_Types import Customer
from .forms import CustomerForm


# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            employeeForm(request)
            username = form.cleaned_data.get('userName')
            password = form.cleaned_data.get('passwordHash')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'frontend/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'frontend/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'frontend/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'frontend/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'frontend/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')


def customerForm(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                cust = Customer(**form.cleaned_data)
                if try_to_save(model=cust, form=form, request=request):
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
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.POST)
        if form.is_valid():
            name = Name(**form.name.cleaned_data)
            address = Address(**form.address.cleaned_data)

            emp = Employee(**form.cleaned_data, name=name, address=address)
            print(Employee.objects.filter(userName=str(emp.userName)))

            try:
                emp.save()
                messages.success(request, 'Added Employee')
                return HttpResponseRedirect('')
            except NotUniqueError as e:
                if Employee.objects.filter(userName=str(emp.userName)).count() > 0:
                    print('userName is not unique')
                    form.add_error('userName', 'Not unique.')
                if Employee.objects.filter(email=str(emp.email)).count() > 0:
                    print('email is not unique')
                    form.add_error('email', 'Not unique.')
                return render(request, 'frontend/employeeForm.html', {'form': form})
        return render(request, 'frontend/employeeForm.html', {'form': form})
    else:
        pass
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


def try_to_save(model, form, request):
    try:
        model.save()
        messages.success(request, 'Successfully added {}.'.format(model.__class__.name))
        return True

    except mongoengine.errors.NotUniqueError as e:
        for field in e.args:
            print(field)
            field_name = re.sub('.+?(?=index\:\ ){1}(index\:\ )|(\_.*)', '', field)
            form.add_error(field_name, 'Must be unique')
        return False
