# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import ListField, ReferenceField

from Class_Types.base_record import BaseRecord
import time as t


class MaterialList(BaseRecord):
    fkMaterialItem = ListField(ReferenceField('MaterialItem'))
