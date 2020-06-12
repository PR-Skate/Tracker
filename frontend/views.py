import json
import re
import mongoengine
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from mongoengine import GridFSProxy
from mongoengine.errors import *

from .forms import *


def process_view(request, model_class, form_class, id=None):
    if request.method == 'POST':
        form = form_class(request.POST, request)
        if form.is_valid():
            model_instance = form.to_model()
            if try_to_save(instance=model_instance, form=form, request=request):
                form.data = dict()
                return render(request, 'frontend/form_template_python.html',
                              {"field_information_list": model_class.get_field_information(), 'form': form})
        return render(request, 'frontend/form_template_python.html',
                      {"field_information_list": model_class.get_field_information(), 'form': form})
    elif id:
        id = id.strip('#')
        model_instance = model_class.objects.get(id=id)
        form = form_class(model_instance.get_form_data())
        return render(request, 'frontend/form_template_python.html',
                      {"field_information_list": model_class.get_field_information(),
                       'model_name': model_class.__name__, 'form': form})
    else:
        return render(request, 'frontend/form_template_python.html',
                      {"field_information_list": model_class.get_field_information()})


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
def customer_form(request, id=None):
    return process_view(request, model_class=Customer, form_class=CustomerForm, id=id)


@login_required
def employee_form(request, id=None):
    return process_view(request, model_class=Employee, form_class=EmployeeForm, id=id)


@login_required
def prep_work_form(request, id=None):
    return process_view(request, model_class=PrepWork, form_class=EmployeeForm, id=id)


@login_required
def store_form(request, id=None):
    return process_view(request, model_class=Store, form_class=StoreForm, id=id)



@login_required
def work_order_form(request, id=None):
    return process_view(request, model_class=WorkOrder, form_class=WorkOrderForm, id=id)


@login_required
def work_order_status_form(request, id=None):
    return process_view(request, model_class=WorkOrderStatus, form_class=WorkOrderStatusForm, id=id)


@login_required
def micro_region_form(request, id=None):
    return process_view(request, model_class=MicroRegionCode, form_class=MicroRegionForm, id=id)


@login_required
def region_form(request, id=None):
    return process_view(request, model_class=RegionCode, form_class=RegionForm, id=id)


''' Needs to be verified after conflicts resolved'''


@login_required
def scope_of_work_form(request, id=None):
    return process_view(request, model_class=ScopeOfWork, form_class=ScopeOfWorkForm, id=id)


@login_required
def scope_of_work_status_form(request, id=None):
    return process_view(request, model_class=ScopeOfWorkStatus, form_class=ScopeOfWorkStatusForm, id=id)


@login_required
def labor_item_form(request, id=None):
    return process_view(request, model_class=LaborItem, form_class=LaborItemForm, id=id)


@login_required
def article_number_state_form(request):
    if request.method == "POST":
        form = ArticleNumberStateForm(request.POST, request)
        if form.is_valid():
            article = ArticleNumberState(**form.cleaned_data)
            if try_to_save(instance=article, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/form_template_python.html',
                      {"field_information_list": ArticleNumberState.get_field_information(), 'form': form})
    return render(request, 'frontend/form_template_python.html',
                  {"field_information_list": ArticleNumberState.get_field_information()})



@login_required
def article_number_form(request, id=None):
    return process_view(request, model_class=ArticleNumber, form_class=ArticleNumberForm, id=id)


@login_required
def material_item_form(request, id=None):
    return process_view(request, model_class=MaterialItem, form_class=MaterialItemForm, id=id)


@login_required
def material_list_form(request):
    if request.method == "POST":
        form = MaterialListForm(request.POST, request)
        if form.is_valid():
            item = MaterialList(**form.cleaned_data)
            if try_to_save(instance=item, form=form, request=request):
                return HttpResponseRedirect('')
        return render(request, 'frontend/form_template_python.html',
                      {"field_information_list": MaterialList.get_field_information(), 'form': form})
    return render(request, 'frontend/form_template_python.html',
                  {"field_information_list": MaterialList.get_field_information()})


@login_required
def location_in_store_form(request, id=None):
    return process_view(request, model_class=LocationInStore, form_class=LocationInStoreForm, id=id)


@login_required
def order_material_form(request, id=None):
    return process_view(request, model_class=OrderMaterial, form_class=OrderMaterialForm, id=id)


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
    fields_dictionary = dict()
    for record in records:
        print('id: {}'.format(record.id), end='\n')
        attributes = dict()
        for field in fields:
            field_name = record._reverse_db_field_map.get(field)
            attributes.update(
                {field.strip('_'): record.__getattribute__(field_name)})
            fields_dictionary.update({field.strip('_'): model._fields[field_name].__class__.__name__})
        instances.append(attributes)

    return render(request, 'frontend/table_template.html',
                  {'table_name': model.__name__, 'fields': [x.strip('_') for x in fields], 'instances': instances,
                   'token': request.user, 'fields_dictionary': json.dumps(fields_dictionary)})


def generate_form_render(model, request):  # TODO JUST WRONG
    records = model.objects.filter(**request.GET.dict())
    fields = model.get_fields(get_id=True)
    instances = list()
    fields_dictionary = dict()
    for record in records:
        print('id: {}'.format(record.id), end='\n')
        attributes = dict()
        for field in fields:
            field_name = record._reverse_db_field_map.get(field)
            attributes.update(
                {field.strip('_'): record.__getattribute__(field_name)})
            fields_dictionary.update({field.strip('_'): model._fields[field_name].__class__.__name__})
        instances.append(attributes)

    return render(request, 'frontend/table_template.html',
                  {'table_name': model.__name__, 'fields': [x.strip('_') for x in fields], 'instances': instances,
                   'token': request.user, 'fields_dictionary': json.dumps(fields_dictionary)})


def try_to_save(instance, form, request):
    try:
        if hasattr(instance, 'id'):
            instance.update()
        else:
            instance.save()
        messages.success(request, 'Successfully added {}.'.format(instance.__class__.__name__))
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
    except Exception as e:
        for field in e.errors:
            print(field)
            field_name = re.sub('.+?(?=index\:\ ){1}(index\:\ )|(\_.*)', '', field)
            form.add_error(field_name, 'Something went wrong.')
            form.add_error(field_name, field)
