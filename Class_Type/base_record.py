# Created By: Chase Crossley
# Created On: 05/07/2020

import time as t
from typing import Final
from bson import ObjectId as ObjectID
from pymongo import MongoClient


class BaseRecord(object):
    def __init__(self, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):
        self._createdUser = createdUser
        self._createdTimestamp = createdTimestamp
        if lastModifiedUser:
            self._lastModifiedUser = lastModifiedUser
        else:
            self._lastModifiedUser = createdUser
        self._lastModifiedTimestamp = lastModifiedTimestamp
        if objectId:
            self._objectId = objectId

    # getters
    def get_created_user(self):
        return self.createdUser

    def get_created_timestamp(self):
        return self.createdTimestamp

    def get_last_modified_user(self):
        return self.lastModifiedUser

    def get_last_modified_timestamp(self):
        return self.lastModifiedTimestamp

    def get_object_id(self):
        if hasattr(self, 'objectId'):
            return self.objectId
        return None

    # setters
    def set_created_user(self, username):
        if not username:
            raise ValueError("username must have value. username: {0}".format(username))
        self.createdUser = username

    def set_created_timestamp(self, time):
        if not isinstance(time, t.time().__class__):
            raise ValueError("time must have value. username: {0}".format(time))
        self.createdTimestamp = time

    def set_last_modified_user(self, username):
        if not username:
            raise ValueError("username must have value. username: {0}".format(username))
        self.lastModifiedUser = username

    def set_last_modified_timestamp(self, time):
        if not isinstance(time, t.time().__class__):
            raise ValueError("time must have value. username: {0}".format(time))
        self.lastModifiedTimestamp = time

    def set_object_id(self, objectId):
        self.objectId = ObjectID(objectId)

    # creating a property objects
    _createdUser: Final = property(get_created_user, set_created_user)
    _createdTimestamp: Final = property(get_created_timestamp, set_created_timestamp)
    _lastModifiedUser = property(get_last_modified_user, set_last_modified_user)
    _lastModifiedTimestamp = property(get_last_modified_timestamp, set_last_modified_timestamp)
    _objectId: Final = property(get_object_id, set_object_id)

    def insert_to_col(self):
        if self._objectId is not None:
            raise Exception("The object has an objectId, this means it was  inserted into the database already.")
        else:
            col = self._connect_to_col()
            result = col.insert_one(self.__dict__)
            self._objectId = result.inserted_id

    def update_to_col(self):
        if self._objectId is None:
            raise Exception("The object does not have an objectId, this means it was  inserted into the database already.")
        else:
            col = self._connect_to_col()
            query = {"_id": self._objectId}
            new_values = {"$set" : self.__dict__ }
            col.update_one(query, new_values)

            print(col.find_one(filter=query))

    def delete_from_col(self):
        if self._objectId is None:
            raise Exception("The object does not have an objectId, this means it was  inserted into the database already.")
        else:
            col = self._connect_to_col()
            query = {"_id": self._objectId}
            col.delete_one(filter=query)

            print(col.find_one(filter=query))


    def _connect_to_col(self):
        client = MongoClient(
            'mongodb://root:6iskvVzSpjcGjOcB8Qfm7htg1@138.68.22.230:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
        col = client["Tracker"][self.__class__.__name__]
        return col

