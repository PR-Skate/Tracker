# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, ListField

from Class_Types.base_record import BaseRecord


class MaterialItem(BaseRecord):
    materialArticleNumber = StringField(required=True)
    description = ListField(StringField(required=True), max_length=7, required=True)
