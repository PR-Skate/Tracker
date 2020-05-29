import mongoengine
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from mongoengine.errors import *

from .forms import *


# Create your views here.
@login_required
def index(request):
    print('{user} is authenticated: {auth}'.format(user=request.user, auth=request.user.is_authenticated))
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
        username = request.POST['userName']
        password = request.POST['passwordHash']
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


@login_required
def customerForm(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request)
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


@login_required
def employeeForm(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request)
        if form.is_valid():
            name = Name(**form.name.cleaned_data)
            address = Address(**form.address.cleaned_data)

            emp = Employee(**form.cleaned_data, name=name, address=address)
            print(Employee.objects.filter(userName=str(emp.userName)))

            try:
                emp.save()
                messages.success(request, 'Added Employee')
                return HttpResponseRedirect('')
            except NotUniqueError:
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


@login_required
def prepWorkForm(request):
    return render(request, 'frontend/prepWorkForm.html')


@login_required
def sowForm(request):
    return render(request, 'frontend/sowForm.html')


@login_required
def storeForm(request):

    cust = Customer.objects.all()
    region_code = RegionCode.objects.all()
    micro_region_code = MicroRegionCode.objects.all()
    if request.method == "POST":
        form = StoreForm(request.POST, request)
        if form.is_valid():
            #print(form.cleaned_data)
            storeManagerName = Name(**form.storeManagerName.cleaned_data)
            opsManagerName = Name(**form.opsManagerName.cleaned_data)
            managerName = Name(**form.managerName.cleaned_data)
            overnightManagerName = Name(**form.overnightManagerName.cleaned_data)
            address = Address(**form.address.cleaned_data)
            inspectionDueDates= form.inspectionDueDates.cleaned_data['inspectionDueDates'].split('|')
            installationDueDates= form.installationDueDates.cleaned_data['installationDueDates'].split('|')
            overnightAccess = form.overnightAccess.cleaned_data['overnightAccess']
            store = Store(**form.cleaned_data, storeManagerName=storeManagerName, opsManagerName=opsManagerName,
                          managerName=managerName, overnightManagerName=overnightManagerName, address=address,
                          inspectionDueDates=inspectionDueDates, installationDueDates=installationDueDates, overnightAccess=overnightAccess)
            store.save()

        return render(request, 'frontend/storeForm.html',
                      {'form': form, 'region_code': region_code, 'micro_region_code': micro_region_code, 'cust': cust})
    return render(request, 'frontend/storeForm.html',{'region_code': region_code, 'micro_region_code': micro_region_code, 'cust': cust})


@login_required
def workOrderForm(request):
    return render(request, 'frontend/workOrderForm.html')


""""REPORTS"""


@login_required
def customerReport(request):
    if request.method == "GET":
        return generate_table_render(model=Customer, request=request)


@login_required
def storeReport(request):
    if request.method == "GET":
        return generate_table_render(model=Store, request=request)


@login_required
def sowReport(request):
    if request.method == "GET":
        return generate_table_render(model=ScopeOfWork, request=request)


@login_required
def employeeReport(request):
    if request.method == "GET":
        return generate_table_render(model=Employee, request=request)


@login_required
def workOrderReport(request):
    if request.method == "GET":
        return generate_table_render(model=WorkOrder, request=request)


@login_required
def articleNumberReport(request):
    if request.method == "GET":
        return generate_table_render(model=ArticleNumber, request=request)


@login_required
def articleNumberStateReport(request):
    if request.method == "GET":
        return generate_table_render(model=ArticleNumberState, request=request)


@login_required
def laborItemReport(request):
    if request.method == "GET":
        return generate_table_render(model=LaborItem, request=request)


@login_required
def materialItemReport(request):
    if request.method == "GET":
        return generate_table_render(model=MaterialItem, request=request)


@login_required
def materialListReport(request):
    if request.method == "GET":
        return generate_table_render(model=MaterialList, request=request)


@login_required
def orderMaterialReport(request):
    if request.method == "GET":
        return generate_table_render(model=OrderMaterial, request=request)


@login_required
def locationInStoreReport(request):
    if request.method == "GET":
        return generate_table_render(model=LocationInStore, request=request)


@login_required
def sowStatusReport(request):
    if request.method == "GET":
        return generate_table_render(model=ScopeOfWorkStatus, request=request)


@login_required
def microRegionCodeReport(request):
    if request.method == "GET":
        return generate_table_render(model=MicroRegionCode, request=request)


@login_required
def regionCodeReport(request):
    if request.method == "GET":
        return generate_table_render(model=RegionCode, request=request)


@login_required
def prepWorkReport(request):
    if request.method == "GET":
        return generate_table_render(model=PrepWork, request=request)


@login_required
def schedulingWorkReport(request):
    if request.method == "GET":
        return generate_table_render(model=SchedulingWork, request=request)


@login_required
def workOrderStatusReport(request):
    if request.method == "GET":
        return generate_table_render(model=WorkOrderStatus, request=request)


def generate_table_render(model, request):
    print(model.__name__)
    records = model.objects.filter(**request.GET.dict())
    fields = model.get_fields()
    instances = list()
    for record in records:
        print('id: {}'.format(record.id), end='\n')
        attributes = {}
        for field in fields:
            field_name = record._reverse_db_field_map.get(field)
            attributes.update({field: record.__getattribute__(field_name)})

        instances.append(attributes)

    return render(request, 'frontend/table_temp.html',
                  {'table_name': model.__name__, 'fields': model.get_fields(), 'instances': instances})


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
