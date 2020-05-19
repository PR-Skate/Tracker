# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, DecimalField, ReferenceField

from .article_number import BaseRecord, ArticleNumber


class ArticleNumberState(BaseRecord):
    state = StringField(max_length=2, min_length=2, required=True)
    price = DecimalField(required=True)
    fkArticleNumber = ReferenceField(ArticleNumber, required=True, dbref=True)
    meta = {'collection': 'ArticleNumberState'}
