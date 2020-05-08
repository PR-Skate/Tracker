# Created By: Alex Peterson
# Created On: 05/07/2020
#
from Class_Types.base_record import BaseRecord

class Customer(BaseRecord):
    def __init__(self, customerName):
        self._customerName = customerName
        BaseRecord.__init__(self, 'CREATED USER')

    def get_customerName(self):
        return self.customerName

    def set_customerName(self, customer_name):
        self.customerName = customer_name

    _customerName = property(get_customerName, set_customerName)
