"""There’s no limit on how many modules you put in the templatetags package. Just keep in mind that a {% load %}
statement will load tags/filters for the given Python module name, not the name of the app."""
from django import template
from Class_Types import *
import json

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
