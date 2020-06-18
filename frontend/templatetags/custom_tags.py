"""There’s no limit on how many modules you put in the templatetags package. Just keep in mind that a :% load %
statement will load tags/filters for the given Python module name, not the name of the app."""
import json
import os
from os.path import join
from django import template
from django.utils.safestring import mark_safe
from mongoengine.dereference import DBRef
from Class_Types import *

STATIC_FILES_FOR_FIELDS = ['state', 'country']

register = template.Library()


def to_json(query_set):
    temp = json.loads(query_set.to_json())
    for i in range(query_set._len):
        dictionary = temp[i]
        for key, value in dictionary.items():
            if isinstance(value, dict) and '$ref' in value.keys():
                dictionary.update({key: query_set[i].__getattribute__(key)})
    return temp


@register.simple_tag
def search(model_name, *args, **kwargs):
    model = globals()[model_name]
    return to_json(model.objects.filter(**kwargs))


@register.simple_tag
def generateHtmlField(field_information, form=None, *args, **kwargs):
    field_type = getFieldType(field_information)
    successful_add = False
    if hasattr(kwargs, "messages"):
        storage = kwargs["messages"]
        for message in storage:
            successful_add = 'success' == message.tags

    if isBasicFieldType(field_type) and not field_information.hidden:
        data = '""'
        if form and form.data and not successful_add:
            if field_type != 'file':
                data = f'"{form.data.get(field_information.model_name)}"'
            else:
                data = f'"{form.FILES.get(field_information.model_name)}"'

        field = f'<label>{field_information.name}</label><br>\n\
                <input type="{field_type if not field_information.hidden else "hidden"}" value={data if field_type != "checkbox" else True} name="{field_information.model_name}" {"required" if field_information.required else ""}><br><br>\n'

        if field_information.name.lower() in STATIC_FILES_FOR_FIELDS:
            field = get_field_from_static_file(field_information)
    elif not field_information.hidden:
        if field_type == "select":
            field = makeSelectContainer(field_information)

        elif field_type == 'subform':
            field = makeSubForm(field_information)
        elif field_type == 'list_field':
            field = makeListField(field_information)
        else:
            field = ''
    elif field_information.hidden:
        data = '""'
        if form and form.data and not successful_add:
            if field_type != 'file':
                data = f'"{form.data.get(field_information.model_name) if not isinstance(form.data.get(field_information.model_name), DBRef) else form.data.get(field_information.model_name).id}"'
            else:
                data = f'"{form.FILES.get(field_information.model_name)}"'

        field = f'<input type="hidden" value={data if field_type != "checkbox" else True} name="{field_information.model_name}">\n'
    else:
        field = ''
    return mark_safe(field)


def get_field_from_static_file(field_information, data=None):
    field = ''
    with open(os.path.abspath(
            join('frontend', 'templates', 'frontend', 'helpers', f'{field_information.name.lower()}.html'))) as f:
        line = f.readline()
        while line:
            if '<select' in line:
                line = line.replace(field_information.name.lower(), field_information.model_name)
            elif '<option value="none"' in line and data:
                line = line.replace('selected', '')
            elif data and data in line:
                line = line.replace('">', '"selected>')
            field += line
            line = f.readline()
    return field


@register.simple_tag
def makeSelectContainer(field_information, data=None):
    options = [f'<option value="" {"selected" if not data else ""} disabled>{field_information.name}</option>']
    instances = getInstances(field_information)
    if instances:
        for instance in instances:
            option = f'\
                    <option value={instance.id} {"selected" if data == instance.id else ""} >{str(instance)}</option>\n'
            options.append(option)
        other = '<option value="Other">Other</option>'
        options.append(other)
    options_string = "\n".join(options)

    selectContainer = f'<label for="{field_information.model_name}">{field_information.name}</label>\n\
            <select name="{field_information.model_name}" class="selectpicker" data-live-search="true" required>n\n\
                 {options_string}\n\
            </select><br><br>'
    return selectContainer


@register.simple_tag
def getInstances(field_information):
    model = globals()[field_information.model]

    if field_information.filter:
        result = model.objects.filter(field_information.filter)
    else:
        result = model.objects.all()

    if not result:
        result = None
    return result


def makeSubForm(field_information):
    field = f'<br><label for="{field_information.model_name}">{field_information.name}</label>\n<hr>'
    sub_form_field_list = list()
    for sub_form_field_information in field_information.sub_form_fields_information:
        sub_form_field_information.model_name = field_information.model_name + "." + sub_form_field_information.model_name
        sub_form_field_list.append(generateHtmlField(sub_form_field_information))
    return field + '\n'.join(sub_form_field_list) + '\n<hr> <br><br><br>\n'


def makeListField(field_information):
    if field_information.list_choices:  # Needs to be check mark fields
        field = f'<label for="">{field_information.name}</label><br><br>\n\''
        for value, display_name in field_information.list_choices:
            field += f'<input type="checkbox" id="{field_information.model_name}" name="{field_information.model_name}" value=\'{value}\' style="margin-left: 4em" unchecked>\n\
            <label for="">{display_name}</label><br><br>'
    else:  # needs to add as many fields as needed
        field_type = getFieldType(type=field_information.list_field_type)
        field = f'<label for="">{field_information.name}</label><br>\n\
            <input type="{field_type}" name="{field_information.model_name}"><br>\n\
            <div id = "{field_information.model_name}" name = "{field_information.model_name}"></div>\n\
            <input type="button" onclick="lib.add(\'{field_information.model_name}\',\'{field_type}\', \'{field_information.model_name}\' )" value="Add">\n\
            <input type="button" onclick="lib.remove(\'{field_information.model_name}\')" value="Remove"> <br> <br>'

    return field


def isBasicFieldType(field_type):
    return field_type != "select" and field_type != "subform" and field_type != "list_field"


@register.simple_tag
def getFieldType(field_information=None, type=None):
    fieldTypes = {'IntField': 'number', 'DecimalField': 'number', 'BooleanField': 'checkbox',
                  'ReferenceField': 'select',
                  'ImageField': 'file', 'FileField': 'file', 'DateField': 'date', 'DateTimeField': 'datetime-local',
                  'StringField': 'text', 'EmailField': 'email', 'EmbeddedDocumentField': 'subform',
                  'ListField': 'list_field', 'ObjectIdField': 'text'
                  }
    if field_information:
        assert type is None
        type = field_information.type

    if type in fieldTypes.keys():
        return fieldTypes.get(type)
    return None


# This comment is to force upload to server
@register.simple_tag
def getSearchFilters(field_information=None, type=None):
    fieldType = None
    if field_information:
        assert type is None
        fieldType = getFieldType(field_information=field_information)

    elif type:
        fieldType = getFieldType(type=type)

    filters = {
        "number": ['less than', 'greater than', 'is', 'is not'],
        "checkBox": ['is true', 'is false'],
        'select': [],
        'file': [],
        'date': ['Is', 'Is Not', 'Is Emtpy', 'Is Not Empty', 'Before', 'After', 'Between', 'Yesterday', 'Today',
                 'Tomorrow', 'Last 7 Days', 'Last 30 Days', 'Last 60 Days', 'Last 90 Days', 'Last 120 Days',
                 'Last N Days', 'Last Week', 'This Week', 'Next Week', 'Current and Previous Week',
                 'Current and Next Week', 'Last N weeks', 'Next N Weeks', 'Last Week', 'This Month', 'Next Month',
                 'Current and Previous Month', 'Current and Next Month', 'Last N Months', 'Next N Months', 'Last Year',
                 'This Year', 'Next Year', 'Current and Previous Year', 'Current and Next Year', 'Last N Years',
                 'Next N Years'],
        'datetime-local': ['before', 'after', 'between', 'on'],
        'text': ['Is', 'Is not', 'Is Empty', 'Is Not Empty', 'Starts With', 'Ends With', 'Like', 'Contains',
                 'Not Contains'],
        'email': ['Is', 'Is not', 'Is Empty', 'Is Not Empty', 'Starts With', 'Ends With', 'Like', 'Contains',
                  'Not Contains'],
        'subform': ['I am a sub form'],
        'list_field': ['Has', 'Does Not Have', 'Is Empty', 'Is Not Empty'],
        'ObjectIdField': ['Is', 'Is not', 'Is Empty', 'Is Not Empty', 'Starts With', 'Ends With', 'Like', 'Contains',
                          'Not Contains']
    }
    return filters.get(fieldType)
