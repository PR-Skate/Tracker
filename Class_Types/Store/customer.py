# Created By: Alex Peterson
# Created On: 05/07/2020
#
from mongoengine import StringField

from Class_Types.base_record import BaseRecord


class Customer(BaseRecord):
    customerName = StringField(max_length=50, required=True, unique=True)
    meta = {'collection': 'Customer'}

    def __str__(self):
        return self.customerName
