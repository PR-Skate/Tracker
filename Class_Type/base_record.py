import time as t
from typing import Final


class BaseRecord(object):
    def __init__(self, created_user, created_timestamp=t.time(), last_modified_user="",
                 last_modified_timestamp=t.time()):
        self.created_user = created_user
        self.created_timestamp = created_timestamp
        if last_modified_user != "":
            self.last_modified_user = last_modified_user
        else:
            self.last_modified_user = created_user
        self.last_modified_timestamp = last_modified_timestamp

    # getters
    def get_created_user(self):
        return self._created_user

    def get_created_timestamp(self):
        return self._created_timestamp

    def get_last_modified_user(self):
        return self._last_modified_user

    def get_last_modified_timestamp(self):
        return self._last_modified_timestamp

    # setters
    def set_created_user(self, username):
        if username == "":
            raise ValueError("username must have value. username: {0}".format(username))
        self._created_user = username

    def set_created_timestamp(self, time):
        if not isinstance(time, t.time().__class__):
            raise ValueError("time must have value. username: {0}".format(time))
        self._created_timestamp = time

    def set_last_modified_user(self, username):
        if username == "":
            raise ValueError("username must have value. username: {0}".format(username))
        self._last_modified_user = username

    def set_last_modified_timestamp(self, time):
        if not isinstance(time, t.time().__class__):
            raise ValueError("time must have value. username: {0}".format(time))
        self._last_modified_timestamp = time

    # creating a property objects
    created_user = property(get_created_user, set_created_user)
    created_timestamp = property(get_created_timestamp, set_created_timestamp)
    last_modified_user = property(get_last_modified_user, set_last_modified_user)
    last_modified_timestamp = property(get_last_modified_timestamp, set_last_modified_timestamp)
