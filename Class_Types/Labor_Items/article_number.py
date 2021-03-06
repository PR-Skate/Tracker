# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, ListField, BooleanField

from Class_Types.base_record import BaseRecord


class ArticleNumber(BaseRecord):
    articleNumber = StringField(max_length=20, required=True, unique=True)
    description = ListField(StringField(), max_length=4, required=True)
    usedByInspectionCompanyButNotPrSkate = BooleanField(default=False)
    capital = BooleanField(default=False)
    meta = {'collection': 'ArticleNumber'}

    def __str__(self):
        description = ' - '.join(self.description)
        return f'{self.articleNumber}: {description}'
