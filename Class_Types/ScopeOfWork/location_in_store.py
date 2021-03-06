# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, BooleanField, ReferenceField, ImageField, ListField

from ..Material_Items import MaterialItem
from ..Store import Store
from ..base_record import BaseRecord


class LocationInStore(BaseRecord):
    department = StringField(required=True, unique_with=['aisle', 'bay', 'tower', 'fkStoreNumber'])
    aisle = StringField(required=True)
    bay = StringField(required=True)
    tower = StringField(required=True)
    level = StringField(required=False, allow_null=True, allow_blank=True, blank=True, null=True)
    other = StringField(required=False)  # only for customers besides home deopt
    plumbingInLocation = BooleanField(default=False)
    plumbingPicturePath = ImageField(default=None)
    plumbingPicturePath2 = ImageField(default=None)
    electricalInLocation = BooleanField(default=False)
    electricalPicturePath = ImageField(default=None)
    electricalPicturePath2 = ImageField(default=None)
    fkMaterialItems = ListField(ReferenceField(MaterialItem, dbref=False))  # should be a series of drop downs
    # where the there are no duplicate references
    fkStoreNumber = ReferenceField(document_type=Store, required=True, dbref=False)
    meta = {'collection': 'LocationInStore'}

    def __str__(self):
        return f'Dept:{self.department} - Bay:{self.bay} - Tower:{self.tower} - Level: {self.level}'
