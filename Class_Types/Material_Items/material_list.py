# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Type.base_record import BaseRecord
import time as t


class MaterialList(BaseRecord):
    def __init__(self, fkMaterialArticleNumber, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):

        self._fkMaterialArticleNumber = fkMaterialArticleNumber

        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_material_article_number(self):
        return self.fkMaterialArticleNumber

    # setters
    def set_material_article_number(self, fkMaterialArticleNumber):
        if not fkMaterialArticleNumber:
            raise ValueError("Material Article Number must have value. Material Article Number: {0}".format(fkMaterialArticleNumber))
        self.fkMaterialArticleNumber = fkMaterialArticleNumber

    # creating a property objects
    _fkMaterialArticleNumber = property(get_material_article_number, set_material_article_number)
