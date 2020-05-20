# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, BooleanField, ReferenceField, ImageField

from ..Store import Store
from ..Material_Items import MaterialList
from ..base_record import BaseRecord


class LocationInStore(BaseRecord):
    department = StringField(required=True, unique_with=['aisle', 'bay', 'tower', 'fkStoreNumber'])
    aisle = StringField(required=True)
    bay = StringField(required=True)
    tower = StringField(required=True)
    level = StringField(required=False, allow_null=True, allow_blank=True, blank=True, null=True)
    plumbingInLocation = BooleanField(default=False)
    plumbingPicturePath = ImageField(default=None)
    plumbingPicturePath2 = ImageField(default=None)
    electricalInLocation = BooleanField(default=False)
    electricalPicturePath = ImageField(default=None)
    electricalPicturePath2 = ImageField(default=None)
    fkMaterialList = ReferenceField(MaterialList, dbref=True)
    fkStoreNumber = ReferenceField(document_type=Store, required=True, dbref=True)
    meta = {'collection': 'LocationInStore'}
