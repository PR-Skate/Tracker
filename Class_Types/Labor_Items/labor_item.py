# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import IntField, ReferenceField
from .article_number_state import BaseRecord, ArticleNumberState

class LaborItem(BaseRecord):
    quantity = IntField(min_value=1)
    fkArticleNumberState = ReferenceField(ArticleNumberState)
    meta = {'collection': 'LaborItem'}
