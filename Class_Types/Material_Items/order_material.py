# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import IntField, ReferenceField
from .material_item import BaseRecord, MaterialItem


class OrderMaterial(BaseRecord):
    quantity = IntField(min_value=1, required=True)
    fkMaterialItem = ReferenceField(MaterialItem, dbref=True)
    meta = {'collection': 'OrderMaterial'}
