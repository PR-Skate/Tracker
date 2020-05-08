# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Types.base_record import BaseRecord
from bson import ObjectId as objectID
import time as t


class ArticleNumberState(BaseRecord):
    def __init__(self, state, price, fkArticleNumber, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):
        self._state = state
        self._price = price
        self._fkArticleNumber = fkArticleNumber
        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_state(self):
        return self.state

    def get_price(self):
        return self.price

    def get_fk_article_number(self):
        return self.fkArticleNumber

    # setters
    def set_state(self, state):
        if not state:
            raise ValueError("State must have value. State: {0}".format(state))
        self.state = state

    def set_price(self, price):
        if price < 0.0:
            raise ValueError("Price must be bigger than 0.0, Price: {0}".format(price))
        self.price = price

    def set_fk_article_number(self, fkArticleNumber):
        if not fkArticleNumber:
            raise ValueError("FK Article Number must have value, FK Article Number: {0}".format(fkArticleNumber))
        self.fkArticleNumber = objectID(fkArticleNumber)

    # creating a property objects
    _state = property(get_state, set_state)
    _price = property(get_price, set_price)
    _fkArticleNumber = property(get_fk_article_number, set_fk_article_number)

