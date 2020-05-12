# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, BooleanField, ReferenceField, ImageField

from Class_Types.base_record import BaseRecord
from bson import ObjectId as objectID
import time as t


class LocationInStore(BaseRecord):
    department = StringField(required=True, unique_with=['aisle', 'bay', 'tower'])
    aisle = StringField(required=True)
    bay = StringField(required=True)
    tower = StringField(required=True)
    level = StringField()
    plumbingInLocation = BooleanField(default=False)
    plumbingPicturePath = ImageField(default=None)
    electricalInLocation = BooleanField(default=False)
    electricalPicturePath = ImageField(default=None)
    fkMaterialList = ReferenceField('MaterialList')
    fkStoreNumber = ReferenceField('Store', required=True)
