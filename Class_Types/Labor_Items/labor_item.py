# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import IntField, ReferenceField

from Class_Types.base_record import BaseRecord


class LaborItem(BaseRecord):
    quantity = IntField(min_value=1)
    fkArticleNumberState = ReferenceField('ArticleNumberState')
    meta = {'collection': 'LaborItem'}
