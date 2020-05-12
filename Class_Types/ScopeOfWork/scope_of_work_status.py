# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField
from Class_Types.base_record import BaseRecord


class ScopeOfWorkStatus(BaseRecord):
    status = StringField(required=True, unique=True)
    meta = {'collection': 'ScopeOfWorkStatus'}
