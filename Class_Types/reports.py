# Created By: Chase Crossley
# Created On: 06/29/2020
#

from mongoengine import StringField, ListField

from Class_Types.Embeded_Documents.embeded_classes import ReportField
from Class_Types.base_record import BaseRecord


class Report(BaseRecord):
    baseReport = StringField(max_length=50, required=True, unique=True)
    name = StringField(max_length=50, required=True, unique=True)
    fields = ListField(ReportField)
    meta = {'collection': 'Report'}

    def __str__(self):
        return f'{self.name} Report'
