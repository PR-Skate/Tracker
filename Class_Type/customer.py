import os
print(os.getcwd())
from Tracker.Class_Type.base_record import BaseRecord

class Customer(BaseRecord):
    def __init__(self, customerName):
        self.customerName = customerName
        BaseRecord.__init__(self, 'CREATED USER')

    def  get_customerName(self):
        return self._customerName

    def set_customerName(self, customer_name):
        self.customerName = customer_name

    customer_name =  property(get_customerName, set_customerName)
    #test