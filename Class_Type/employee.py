# Created By: Alex Peterson
# Created On: 05/07/2020
#
from Class_Type.base_record import BaseRecord


class Employee(BaseRecord):
    # constructor:
    def __init__(self, userName, firstName, lastName, birthDate, address, email, phone, active,
                 password, _type, pin, rateOfPay=-1):
        self._userName = userName
        self._firstName = firstName
        self._lastName = lastName
        self._birthDate = birthDate
        self._address = address
        self._email = email
        self._phone = phone
        self._pin = pin
        self._rateOfPay = rateOfPay
        self._active = active
        self._password = password
        self._type = _type
        BaseRecord.__init__(self, userName)

    # getters:
    def get_user_name(self):
        return self.userName

    def get_first_name(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName

    def get_birth_date(self):
        return self.birthDate

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_pin(self):
        return self.pin

    def get_rate_of_pay(self):
        return self.rateOfPay

    def get_active(self):
        return self.active

    def get_password(self):
        return self.password

    def get_type(self):
        return self.type

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
        self.address = __address

    def set_email(self, __email):
        self.email = __email

    def set_phone(self, __phone):
        self.phone = __phone

    def set_pin(self, __pin):
        self.pin = __pin

    def set_rate_of_pay(self, rate_of_pay):
        self.rateOfPay = rate_of_pay

    def set_active(self, __active):
        self.active = __active

    def set_password(self, __password):
        self.password = __password

    def set_type(self, _type):
        self.type = _type

    _userName = property(get_user_name, set_user_name)
    _firstName = property(get_first_name, set_first_name)
    _lastName = property(get_last_name, set_last_name)
    _birthDate = property(get_birth_date, set_birth_date)
    _address = property(get_address, set_address)
    _email = property(get_email, set_email)
    _phone = property(get_phone, set_phone)
    _pin = property(get_pin, set_pin)
    _rateOfPay = property(get_rate_of_pay, set_rate_of_pay)
    _active = property(get_active, set_active)
    _password = property(get_password, set_password)
    _type = property(get_type, set_type)


e = Employee('Petersonalex99', 'Alex', 'Peterson', '06/16/99', 'MyAddress', 'Alex@gmail.com', '9097056842', True, 'Puppies420', 1234, 15.00)

print(e.userName)
