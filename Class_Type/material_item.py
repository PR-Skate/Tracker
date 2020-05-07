# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Type.base_record import BaseRecord
from bson import ObjectId as objectID
import time as t


class LaborItem(BaseRecord):
    def __init__(self, quantity, fkArticleNumberState, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):
        self._quantity = quantity
        self._fkArticleNumberState = fkArticleNumberState
        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_quantity(self):
        return self.quantity

    def get_fk_article_number_state(self):
        return self.fkArticleNumberState

    # setters

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be bigger than 0.0, Quantity: {0}".format(quantity))
        self.quantity = quantity

    def set_fk_article_number_state(self, fkArticleNumberState):
        if not fkArticleNumberState:
            raise ValueError("FK Article Number State must have value, FK Article Number State: {0}".format(fkArticleNumberState))
        self.fkArticleNumberState = objectID(fkArticleNumberState)

    # creating a property objects
    _quantity = property(get_quantity, set_quantity)
    _fkArticleNumberState = property(get_fk_article_number_state, set_fk_article_number_state)

