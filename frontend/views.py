import re
import mongoengine
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

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
            employee_form(request)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
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


@login_required
def customer_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request)
        if form.is_valid():
            cust = Customer(**form.cleaned_data)
            if try_to_save(model=cust, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/customerForm.html', {'form': form})
    return render(request, 'frontend/customerForm.html')


@login_required
def employee_form(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request)
        if form.is_valid():
            name = Name(**form.name.cleaned_data)
            address = Address(**form.address.cleaned_data)
            emp = Employee(**form.cleaned_data, name=name, address=address)

            if try_to_save(model=emp, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/employeeForm.html', {'form': form})
    return render(request, 'frontend/employeeForm.html')


@login_required
def prep_work_form(request):
    work_order = WorkOrder.objects.all()
    if request.method == "POST":
        form = PrepWorkForm(request.POST, request)
        if form.is_valid():
            prepWork = PrepWork(**form.cleaned_data)
            if try_to_save(model=prepWork, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/prepWorkForm.html', {'form':form, 'work_order': work_order})
    return render(request, 'frontend/prepWorkForm.html', {'work_order': work_order})


@login_required
def store_form(request):
    cust = Customer.objects.all()
    region_code = RegionCode.objects.all()
    micro_region_code = MicroRegionCode.objects.all()
    if request.method == "POST":
        form = StoreForm(request.POST, request)
        if form.is_valid():
            storeManagerName = Name(**form.storeManagerName.cleaned_data)
            opsManagerName = Name(**form.opsManagerName.cleaned_data)
            managerName = Name(**form.managerName.cleaned_data)
            overnightManagerName = Name(**form.overnightManagerName.cleaned_data)
            address = Address(**form.address.cleaned_data)
            inspectionDueDates = form.inspectionDueDates.cleaned_data['inspectionDueDates'].split('|')
            installationDueDates = form.installationDueDates.cleaned_data['installationDueDates'].split('|')
            overnightAccess = form.overnightAccess.cleaned_data['overnightAccess']
            coordinates = Coordinates(**form.coordinates.cleaned_data)
            store = Store(**form.cleaned_data, storeManagerName=storeManagerName, opsManagerName=opsManagerName,
                          managerName=managerName, overnightManagerName=overnightManagerName, address=address,
                          inspectionDueDates=inspectionDueDates, installationDueDates=installationDueDates,
                          overnightAccess=overnightAccess,
                          coordinates=coordinates)
            if try_to_save(model=store, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/storeForm.html',
                      {'form': form, 'region_code': region_code, 'micro_region_code': micro_region_code, 'cust': cust})
    return render(request, 'frontend/storeForm.html',
                  {'region_code': region_code, 'micro_region_code': micro_region_code, 'cust': cust})


@login_required
def work_order_form(request):
    store = Store.objects.all()
    workOrderStatus = WorkOrderStatus.objects.all()
    if request.method == "POST":
        form = WorkOrderForm(data=request.POST, request=request, files=request.FILES)
        if form.is_valid():
            wo = WorkOrder(**form.cleaned_data)
            if try_to_save(model=wo, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/workOrderForm.html', {'form': form, 'store': store})
    return render(request, 'frontend/workOrderForm.html', {'store': store, 'workOrderStatus': workOrderStatus})


@login_required
def work_order_status_form(request):
    if request.method == "POST":
        form = WorkOrderStatusForm(request.POST, request)
        if form.is_valid():
            status = WorkOrderStatus(**form.cleaned_data)
            if try_to_save(model=status, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/workOrderStatusForm.html', {'form': form})
    return render(request, 'frontend/workOrderStatusForm.html')


@login_required
def micro_region_form(request):
    if request.method == 'POST':
        form = MicroRegionForm(request.POST, request)
        if form.is_valid():
            region = MicroRegionCode(**form.cleaned_data)
            if try_to_save(model=region, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/microRegionForm.html', {'form': form})
    return render(request, 'frontend/microRegionForm.html')


@login_required
def region_form(request):
    if request.method == 'POST':
        form = RegionForm(request.POST, request)
        if form.is_valid():
            region = RegionCode(**form.cleaned_data)
            if try_to_save(model=region, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/regionForm.html', {'form': form})
    return render(request, 'frontend/regionForm.html')


''' Needs to be verified afer conflicts resolved'''


@login_required
def scope_of_work_status_form(request):
    if request.method == "POST":
        form = ScopeOfWorkStatusForm(request.POST, request)
        if form.is_valid():
            status = ScopeOfWorkStatus(**form.cleaned_data)
            if try_to_save(model=status, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/scopeOfWorkStatusForm.html', {'form': form})
    return render(request, 'frontend/scopeOfWorkStatusForm.html')


@login_required
def labor_item_form(request):
    if request.method == "POST":
        form = LaborItemForm(request.POST, request)
        if form.is_valid():
            item = LaborItem(**form.cleaned_data)
            if try_to_save(model=item, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/laborItemForm.html', {'form': form})
    return render(request, 'frontend/laborItemForm.html')


@login_required
def article_number_state_form(request):
    if request.method == "POST":
        form = ArticleNumberStateForm(request.POST, request)
        if form.is_valid():
            article = ArticleNumberState(**form.cleaned_data)
            if try_to_save(model=article, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/articleNumberStateForm.html', {'form': form})
    return render(request, 'frontend/articleNumberStateForm.html')


@login_required
def article_number_form(request):
    if request.method == "POST":
        form = ArticleNumberForm(request.POST, request)
        if form.is_valid():
            # will need a special form for the list
            article = ArticleNumber(**form.cleaned_data)
            if try_to_save(model=article, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/articleNumberForm.html', {'form': form})
    return render(request, 'frontend/articleNumberForm.html')


@login_required
def material_item_form(request):
    if request.method == "POST":
        form = MaterialItemForm(request.POST, request)
        if form.is_valid():
            item = MaterialItem(**form.cleaned_data)
            if try_to_save(model=item, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/materialItemForm.html', {'form': form})
    return render(request, 'frontend/materialItemForm.html')


@login_required
def material_list_form(request):
    if request.method == "POST":
        form = MaterialListForm(request.POST, request)
        if form.is_valid():
            item = MaterialList(**form.cleaned_data)
            if try_to_save(model=item, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/materialListForm.html', {'form': form})
    return render(request, 'frontend/materialListForm.html')


@login_required
def location_in_store_form(request):
    if request.method == 'POST':
        form = LocationInStoreForm(data=request.POST, request=request, files=request.FILES)
        if form.is_valid():
            location = LocationInStore(**form.cleaned_data)
            if try_to_save(model=location, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/locationInStoreForm.html', {'form': form})
    return render(request, 'frontend/locationInStoreForm.html')


""""REPORTS"""


@login_required
def customer_report(request):
    if request.method == "GET":
        return generate_table_render(model=Customer, request=request)


@login_required
def store_report(request):
    if request.method == "GET":
        return generate_table_render(model=Store, request=request)


@login_required
def scope_of_work_report(request):
    if request.method == "GET":
        return generate_table_render(model=ScopeOfWork, request=request)


@login_required
def employee_report(request):
    if request.method == "GET":
        return generate_table_render(model=Employee, request=request)


@login_required
def work_order_report(request):
    if request.method == "GET":
        return generate_table_render(model=WorkOrder, request=request)


@login_required
def article_number_report(request):
    if request.method == "GET":
        return generate_table_render(model=ArticleNumber, request=request)


@login_required
def article_number_state_report(request):
    if request.method == "GET":
        return generate_table_render(model=ArticleNumberState, request=request)


@login_required
def labor_item_report(request):
    if request.method == "GET":
        return generate_table_render(model=LaborItem, request=request)


@login_required
def material_item_report(request):
    if request.method == "GET":
        return generate_table_render(model=MaterialItem, request=request)


@login_required
def material_list_report(request):
    if request.method == "GET":
        return generate_table_render(model=MaterialList, request=request)


@login_required
def order_material_report(request):
    if request.method == "GET":
        return generate_table_render(model=OrderMaterial, request=request)


@login_required
def location_in_store_report(request):
    if request.method == "GET":
        return generate_table_render(model=LocationInStore, request=request)


@login_required
def scope_of_work_status_report(request):
    if request.method == "GET":
        return generate_table_render(model=ScopeOfWorkStatus, request=request)


@login_required
def micro_region_code_report(request):
    if request.method == "GET":
        return generate_table_render(model=MicroRegionCode, request=request)


@login_required
def region_code_report(request):
    if request.method == "GET":
        return generate_table_render(model=RegionCode, request=request)


@login_required
def prep_work_report(request):
    if request.method == "GET":
        return generate_table_render(model=PrepWork, request=request)


@login_required
def scheduling_work_report(request):
    if request.method == "GET":
        return generate_table_render(model=SchedulingWork, request=request)


@login_required
def work_order_status_report(request):
    if request.method == "GET":
        return generate_table_render(model=WorkOrderStatus, request=request)


def generate_table_render(model, request):
    print(model.__name__)
    records = model.objects.filter(**request.GET.dict())
    fields = model.get_fields(get_id=True)
    instances = list()
    for record in records:
        print('id: {}'.format(record.id), end='\n')
        attributes = {}
        for field in fields:
            field_name = record._reverse_db_field_map.get(field)
            attributes.update(
                {field.strip('_'): record.__getattribute__(field_name)})

        instances.append(attributes)

    return render(request, 'frontend/table_temp.html',
                  {'table_name': model.__name__, 'fields': [x.strip('_') for x in fields], 'instances': instances,
                   'token': request.user})


def try_to_save(model, form, request):
    try:
        model.save()
        messages.success(request, 'Successfully added {}.'.format(model.__class__.__name__))
        return True
    except mongoengine.errors.NotUniqueError as e:
        for field in e.args:
            field_name = re.sub('.+?(?=index\:\ ){1}(index\:\ )|(\_.*)', '', field)
            form.add_error(field_name, 'Must be unique')
        return False
    except mongoengine.errors.ValidationError as e:
        for field in e.errors:
            field_name = re.sub('.+?(?=index\:\ ){1}(index\:\ )|(\_.*)', '', field)
            form.add_error(field_name, 'Must be unique')
        return False
