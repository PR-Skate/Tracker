# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, ListField

from Class_Types.base_record import BaseRecord


class ArticleNumber(BaseRecord):
    articleNumber = StringField(max_length=20, required=True)
    description = ListField(StringField, max_length=4)
    meta = {'collection': 'ArticleNumber'}
