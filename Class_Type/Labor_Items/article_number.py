# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Type.base_record import BaseRecord
import time as t


class ArticleNumber(BaseRecord):
    def __init__(self, articleNumber, description, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):
        self._articleNumber = articleNumber
        self._description = description
        if not lastModifiedUser:
            BaseRecord.__init__(self, createdUser)
        else:
            BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_article_number(self):
        return self.articleNumber

    def get_description(self):
        return self.description

    # setters
    def set_article_number(self, articleNumber):
        if not articleNumber:
            raise ValueError("Article Number must have value. Article Number: {0}".format(articleNumber))
        self.articleNumber = articleNumber

    def set_description(self, description):
        if not description:
            raise ValueError("description must have a length of at least 1. description: {0}".format(description))
        self.description = description

    # creating a property objects
    _articleNumber = property(get_article_number, set_article_number)
    _description = property(get_description, set_description)
