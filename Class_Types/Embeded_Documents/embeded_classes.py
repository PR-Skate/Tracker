import re
from mongoengine import StringField, EmbeddedDocument


class Address(EmbeddedDocument):
    addressLineOne = StringField(max_length=150, required=True)
    addressLineTwo = StringField(max_length=150)
    city = StringField(max_length=75, required=True)
    state = StringField(max_length=2, required=True)
    zip = StringField(regex=re.compile('^\d{5}'),max_length=5, required=True)
    country = StringField(max_length=75, required=True)
