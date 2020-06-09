"""There’s no limit on how many modules you put in the templatetags package. Just keep in mind that a :% load %
statement will load tags/filters for the given Python module name, not the name of the app."""
import json
import os
from os.path import join

from django import template
from django.utils.safestring import mark_safe
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

    if isBasicFieldType(field_type):
        data = '""'
        if form and not successful_add:
            if field_type != 'file':
                data = f'"{form.data.get(field_information.model_name)}"'
            else:
                data = f'"{form.FILES.get(field_information.model_name)}"'

        field = f'<label>{field_information.name}</label><br>\n\
                <input type="{field_type}" value={data if field_type != "checkbox" else True} name="{field_information.model_name} {"required" if field_information.required else ""}"><br><br>\n'

        if field_information.name.lower() in STATIC_FILES_FOR_FIELDS:
            field = get_field_from_static_file(field_information)
    else:
        if field_type == "select":
            field = makeSelectContainer(field_information)

        elif field_type == 'subform':
            field = makeSubForm(field_information)
        elif field_type == 'list_field':
            field = makeListField(field_information)
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
            <select name="{field_information.model_name}" required>n\n\
                 {options_string}\n\
            </select><br><br>'
    return selectContainer


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
    field = f'<label for="{field_information.model_name}">{field_information.name}</label>\n<hr>'
    sub_form_field_list = list()
    for sub_form_field_information in field_information.sub_form_fields_information:
        sub_form_field_list.append(generateHtmlField(sub_form_field_information))
    return field + '\n'.join(sub_form_field_list) + '\n<hr>\n'


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


def getFieldType(field_information=None, type=None):
    fieldTypes = {'IntField': 'number', 'DecimalField': 'number', 'BooleanField': 'checkbox',
                  'ReferenceField': 'select',
                  'ImageField': 'file', 'FileField': 'file', 'DateField': 'date', 'DateTimeField': 'datetime-local',
                  'StringField': 'text', 'EmailField': 'email', 'EmbeddedDocumentField': 'subform',
                  'ListField': 'list_field'
                  }
    if field_information:
        assert type is None
        type = field_information.type

    if type in fieldTypes.keys():
        return fieldTypes.get(type)
    return None
