import time as t
from typing import Final


class BaseRecord(object):
    def __init__(self, created_user, created_timestamp=t.time(), last_modified_user="",
                 last_modified_timestamp=t.time()):
        self.createdUser = created_user
        self.createdTimestamp = created_timestamp
        if last_modified_user != "":
            self.lastModifiedUser = last_modified_user
        else:
            self.lastModifiedUser = created_user
        self.lastModifiedTimestamp = last_modified_timestamp

    # getters
    def _get_created_user(self):
        return self.createdUser

    def _get_created_timestamp(self):
        return self.createdTimestamp

    def _get_last_modified_user(self):
        return self.lastModifiedUser

    def _get_last_modified_timestamp(self):
        return self.lastModifiedTimestamp

    # setters
    def _set_created_user(self, username):
        if username == "":
            raise ValueError("username must have value. username: {0}".format(username))
        self.createdUser = username

    def _set_created_timestamp(self, time):
        if not isinstance(time, t.time().__class__):
            raise ValueError("time must have value. username: {0}".format(time))
        self.createdTimestamp = time

    def _set_last_modified_user(self, username):
        if username == "":
            raise ValueError("username must have value. username: {0}".format(username))
        self.lastModifiedUser = username

    def _set_last_modified_timestamp(self, time):
        if not isinstance(time, t.time().__class__):
            raise ValueError("time must have value. username: {0}".format(time))
        self.lastModifiedTimestamp = time

    # creating a property objects
    created_user: Final = property(_get_created_user, _set_created_user)
    created_timestamp: Final = property(_get_created_timestamp, _set_created_timestamp)
    last_modified_user = property(_get_last_modified_user, _set_last_modified_user)
    last_modified_timestamp = property(_get_last_modified_timestamp, _set_last_modified_timestamp)
