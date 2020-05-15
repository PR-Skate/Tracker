# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import IntField, ReferenceField

from Class_Types import MaterialItem
from Class_Types.base_record import BaseRecord


class OrderMaterial(BaseRecord):
    quantity = IntField(min_value=1, required=True)
    fkMaterialItem = ReferenceField(MaterialItem)
    meta = {'collection': 'OrderMaterial'}
