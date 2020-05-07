# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Type.base_record import BaseRecord
import time as t


class MaterialItem(BaseRecord):
    def __init__(self, materialArticleNumber, description, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):

        self._materialArticleNumber = materialArticleNumber
        self._description = description

        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_material_article_number(self):
        return self.materialArticleNumber

    def get_description(self):
        return self.description

    # setters
    def set_material_article_number(self, materialArticleNumber):
        if not materialArticleNumber:
            raise ValueError("Article Number must have value. Article Number: {0}".format(materialArticleNumber))
        self.materialArticleNumber = materialArticleNumber

    def set_description(self, description):
        if not description:
            raise ValueError("description must have a length of at least 1. description: {0}".format(description))
        self.description = description

        # creating a property objects

    _materialArticleNumber = property(get_material_article_number, set_material_article_number)
    _description = property(get_description, set_description)
