# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

from mongoengine import StringField

from Class_Types.base_record import BaseRecord


class WorkOrderStatus(BaseRecord):
    # constructor:
    status = StringField(unique=True, max_length=50)
    meta = {'collection': 'WorkOrderStatus'}
