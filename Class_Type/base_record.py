import time as t
from typing import Final
from bson import ObjectId as ObjectID


class BaseRecord(object):
    def __init__(self, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):
        self.createdUser = createdUser
        self.createdTimestamp = createdTimestamp
        if lastModifiedUser:
            self.lastModifiedUser = lastModifiedUser
        else:
            self.lastModifiedUser = createdUser
        self.lastModifiedTimestamp = lastModifiedTimestamp
        if objectId:
            self.objectId = objectId

    # getters
    def get_created_user(self):
        return self._createdUser

    def get_created_timestamp(self):
        return self._createdTimestamp

    def get_last_modified_user(self):
        return self._lastModifiedUser

    def get_last_modified_timestamp(self):
        return self._lastModifiedTimestamp

    def get_object_id(self):
        if hasattr(self, 'objectId'):
            return self._objectId
        return None

    # setters
    def set_created_user(self, username):
        if not username:
            raise ValueError("username must have value. username: {0}".format(username))
        self._createdUser = username

    def set_created_timestamp(self, time):
        if not isinstance(time, t.time().__class__):
            raise ValueError("time must have value. username: {0}".format(time))
        self._createdTimestamp = time

    def set_last_modified_user(self, username):
        if not username:
            raise ValueError("username must have value. username: {0}".format(username))
        self._lastModifiedUser = username

    def set_last_modified_timestamp(self, time):
        if not isinstance(time, t.time().__class__):
            raise ValueError("time must have value. username: {0}".format(time))
        self._lastModifiedTimestamp = time

    def set_object_id(self, objectId):
        if hasattr(self, 'objectId'):
            self._objectId = ObjectID(objectId)

    # creating a property objects
    createdUser: Final = property(get_created_user, set_created_user)
    createdTimestamp: Final = property(get_created_timestamp, set_created_timestamp)
    lastModifiedUser = property(get_last_modified_user, set_last_modified_user)
    lastModifiedTimestamp = property(get_last_modified_timestamp, set_last_modified_timestamp)
    objectId: Final = property(get_object_id, set_object_id)

