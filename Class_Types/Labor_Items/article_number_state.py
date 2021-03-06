# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, DecimalField, ReferenceField

from .article_number import BaseRecord, ArticleNumber


class ArticleNumberState(BaseRecord):  # Need Batch Upload
    state = StringField(max_length=2, min_length=2, required=True, unique_with="fkArticleNumber")
    price = DecimalField(required=True)
    fkArticleNumber = ReferenceField(ArticleNumber, required=True, dbref=False)
    meta = {'collection': 'ArticleNumberState'}

    def __str__(self):
        return f'{self.state} {self.fkArticleNumber.description}'
