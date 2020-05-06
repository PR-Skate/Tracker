from Class_Type.base_record import BaseRecord


class Employee(BaseRecord):
    # constructor:
    def __init__(self, userName, firstName, lastName, birthDate, address, email, phone, pin, rateOfPay, active,
                 password):
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
        self.passwordHash = password
        BaseRecord.__init__(self, 'Alex')

    # getters:
    def _get_user_name(self):
        return self.userName

    def _get_first_name(self):
        return self.firstName

    def _get_last_name(self):
        return self.lastName

    def _get_birth_date(self):
        return self.birthDate

    def _get_address(self):
        return self.address

    def _get_email(self):
        return self.email

    def _get_phone(self):
        return self.phone

    def _get_pin(self):
        return self.pin

    def _get_rate_of_pay(self):
        return self.rateOfPay

    def _get_active(self):
        return self.active

    def _get_password(self):
        return self.passwordHash

    # setters:
    def _set_user_name(self, user_name):
        self.userName = user_name

    def _set_first_name(self, first_name):
        self.firstName = first_name

    def _set_last_name(self, last_name):
        self.lastName = last_name

    def _set_birth_date(self, birth_date):
        self.birthDate = birth_date

    def _set_address(self, address):
        self.address.addressLineOne = address.get("addressLineOne")
        self.address.addressLineTwo = address.get("addressLineOTwo")
        self.address.city = address.get("city")
        self.address.state = address.get("state")
        self.address.zip = address.get("zip")
        self.address.country = address.get("country")

    def _set_email(self, email):
        self.email = email

    def _set_phone(self, phone):
        self.phone = phone

    def _set_pin(self, pin):
        self.pin = pin

    def _set_rate_of_pay(self, rate_of_pay):
        self.rateOfPay = rate_of_pay

    def _set_active(self, active):
        self.active = active

    def _set_password(self, password):
        self.passwordHash = password

    _user_name = property(_get_user_name, _set_user_name)
    _first_name = property(_get_first_name, _set_first_name)
    _last_name = property(_get_last_name, _set_last_name)
    _birth_date = property(_get_birth_date, _set_birth_date)
    _address = property(_get_address, _set_address)
    _email = property(_get_email, _set_email)
    _phone = property(_get_phone, _set_phone)
    _pin = property(_get_pin, _set_pin)
    _rate_of_pay = property(_get_rate_of_pay, _set_rate_of_pay)
    _active = property(_get_active, _set_active)
    _password_hash = property(_get_password, _set_password)
