# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Types.base_record import BaseRecord
from bson import ObjectId as objectID
import time as t


class OrderMaterial(BaseRecord):
    def __init__(self, quantity, fkMaterialArticleNumber, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):
        self._quantity = quantity
        self._fkMaterialArticleNumber = fkMaterialArticleNumber
        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_quantity(self):
        return self.quantity

    def get_fk_article_number_state(self):
        return self.fkMaterialArticleNumber

    # setters

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be bigger than 0.0, Quantity: {0}".format(quantity))
        self.quantity = quantity

    def set_fk_article_number_state(self, fkMaterialArticleNumber):
        if not fkMaterialArticleNumber:
            raise ValueError("FK Material Article Number State must have value, FK Article Number State: {0}".format(fkMaterialArticleNumber))
        self.fkMaterialArticleNumber = objectID(fkMaterialArticleNumber)

    # creating a property objects
    _quantity = property(get_quantity, set_quantity)
    _fkMaterialArticleNumber = property(get_fk_article_number_state, set_fk_article_number_state)

