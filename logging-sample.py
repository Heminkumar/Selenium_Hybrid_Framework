import logging

logging.basicConfig(filename='.//Logs//Employee.log', level=logging.INFO,
                    format='%(levelname)s: %(name)s: %(message)s')

class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        logging.info('Created Employee: {} - {}'.format(self.fullname,self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname (self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee("Hemin", "Patel")
emp_2 = Employee('Ketul','Patel')