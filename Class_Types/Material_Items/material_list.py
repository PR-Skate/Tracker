# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import ListField, ReferenceField
from .material_item import BaseRecord, MaterialItem


class MaterialList(BaseRecord):
    fkMaterialItem = ListField(ReferenceField(MaterialItem, dbref=True))
    meta = {'collection': 'MaterialList'}
