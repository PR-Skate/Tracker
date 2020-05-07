# Created By: Alex Peterson
# Created On: 05/07/2020
#

import os
print(os.getcwd())
from Tracker.Class_Type.base_record import BaseRecord


class Employee(BaseRecord):
    # constructor:
    def __init__(self, userName, firstName, lastName, birthDate, address, email, phone, active,
                 password, pin=0000, rateOfPay=-1):
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.address = address
        self.email = email
        self.phone = phone
        self.pin = pin
        self.rateOfPay = rateOfPay
        self.active = active
        self.password = password
        BaseRecord.__init__(self, userName)

    # getters:
    def get_user_name(self):
        return self._userName

    def get_first_name(self):
        return self._firstName

    def get_last_name(self):
        return self._lastName

    def get_birth_date(self):
        return self._birthDate

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def get_pin(self):
        return self._pin

    def get_rate_of_pay(self):
        return self._rateOfPay

    def get_active(self):
        return self._active

    def get_password(self):
        return self._password

    # setters:
    def set_user_name(self, user_name):
        self.userName = user_name

    def set_first_name(self, first_name):
        self.firstName = first_name

    def set_last_name(self, last_name):
        self.lastName = last_name

    def set_birth_date(self, birth_date):
        self.birthDate = birth_date

    def set_address(self, __address):
        self._address = __address

    def set_email(self, __email):
        self._email = __email

    def set_phone(self, __phone):
        self._phone = __phone

    def set_pin(self, __pin):
        self._pin = __pin

    def set_rate_of_pay(self, rate_of_pay):
        self.rateOfPay = rate_of_pay

    def set_active(self, __active):
        self._active = __active

    def set_password(self, __password):
        self._password = __password

    user_name = property(get_user_name, set_user_name)
    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)
    birth_date = property(get_birth_date, set_birth_date)
    address_ = property(get_address, set_address)
    email_ = property(get_email, set_email)
    phone_ = property(get_phone, set_phone)
    pin_ = property(get_pin, set_pin)
    rate_of_pay_ = property(get_rate_of_pay, set_rate_of_pay)
    active_ = property(get_active, set_active)
    user_passwordname_ = property(get_password, set_password)


e = Employee('Petersonalex99', 'Alex', 'Peterson', '06/16/99', 'MyAddress', 'Alex@gmail.com', '9097056842', True, 'Puppies420', 1234, 15.00)

print(e.userName)
