# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, DecimalField, ReferenceField

from Class_Types.base_record import BaseRecord


class ArticleNumberState(BaseRecord):
    state = StringField(max_length=2, min_length=2, required=True)
    price = DecimalField(required=True)
    fkArticleNumber = ReferenceField('ArticleNumber', required=True)
    meta = {'collection': 'ArticleNumberState'}
