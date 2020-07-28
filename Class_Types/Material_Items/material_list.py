# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import ListField, ReferenceField

from .material_item import BaseRecord, MaterialItem


class MaterialList(BaseRecord):
    fkMaterialItem = ListField(ReferenceField(MaterialItem, dbref=False))
    meta = {'collection': 'MaterialList'}

    def __str__(self):
        description = ', '.join(self.fkMaterialItem)
        return f'{description}'
