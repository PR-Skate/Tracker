# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import IntField, ReferenceField, ImageField

from .article_number_state import BaseRecord, ArticleNumberState


class LaborItem(BaseRecord):
    quantity = IntField(min_value=1)
    extraLaborPhoto = ImageField()
    fkArticleNumberState = ReferenceField(ArticleNumberState, dbref=True)
    meta = {'collection': 'LaborItem'}

    def __str__(self):
        description = ' - '.join(self.fkArticleNumberState.fkArticleNumber.description)
        return f' {description} x {self.quantity} = {self.quantity * self.fkArticleNumberState.price}'
