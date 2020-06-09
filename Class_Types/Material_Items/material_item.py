# Created By: Chase Crossley
# Created On: 05/07/2020
from mongoengine import StringField, ListField

from Class_Types.base_record import BaseRecord


class MaterialItem(BaseRecord):
    materialArticleNumber = StringField(required=True)
    description = ListField(StringField(), max_length=7, required=True)
    meta = {'collection': 'MaterialItem'}

    def __str__(self):
        description = ' - '.join(self.description)
        return f'{self.materialArticleNumber}: {description}'
