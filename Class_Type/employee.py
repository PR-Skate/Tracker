from Class_Type.base_record import BaseRecord


class Employee(BaseRecord):
    # constructor:
    def __init__(self, userName, firstName, lastName, birthDate, address, email, phone, pin, rateOfPay, active,
                 password):
        self.user_name = userName
        self.first_name = firstName
        self.last_name = lastName
        self.birthDate = birthDate
        self.address = address
        self.email = email
        self.phone = phone
        self.pin = pin
        self.rate_of_pay = rateOfPay
        self.active = active
        self.password = password
        BaseRecord.__init__(self, 'Alex')

    # getters:
    def get_user_name(self):
        return self._user_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_birth_date(self):
        return self._birth_date

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def get_pin(self):
        return self._pin

    def get_rate_of_pay(self):
        return self._rate_of_pay

    def get_active(self):
        return self._active

    def get_password(self):
        return self._password

    # setters:
    def set_user_name(self, user_name):
        self._user_name = user_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_birth_date(self, birth_date):
        self._birth_date = birth_date

    def set_address(self, address):
        self._address = address

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone

    def set_pin(self, pin):
        self._pin = pin

    def set_rate_of_pay(self, rate_of_pay):
        self._rate_of_pay = rate_of_pay

    def set_active(self, active):
        self._active = active

    def set_password(self, password):
        self._password = password

    user_name = property(get_user_name, set_user_name)
    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)
    birth_date = property(get_birth_date, set_birth_date)
    address = property(get_address, set_address)
    email = property(get_email, set_email)
    phone = property(get_phone, set_phone)
    pin = property(get_pin, set_pin)
    rate_of_pay = property(get_rate_of_pay, set_rate_of_pay)
    active = property(get_active, set_active)
    user_passwordname = property(get_password, set_password)


e = Employee('Alex', 'Alex', 'Alex', '', '', '', '', '', '', '', '')

print(e.created_timestamp)
