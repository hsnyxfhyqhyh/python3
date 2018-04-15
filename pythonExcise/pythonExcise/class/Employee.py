class Employee:
    """description of class"""
    # does python has a specific way to handle the static variable???
    num_of_emps = 0     # to treat it as a static variable. 
    raise_amt = 1.04    # instance variable 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format (self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    #alternative constructor from method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):        # not like class method or instance variable, no first parameter. 
        if day.weekday() == 5 or day.weekday() == 6:
            return False
   
        return True

emp_1 = Employee('Ying', 'Hu', 50000)
emp_2 = Employee('Xuemei', 'Zhang', 60000)

print(Employee.raise_amt)
emp_1.raise_amt = 1.05

print(emp_1.raise_amt)
print(emp_2.raise_amt)
print('__________________')

# 调用class method也不需要pass第一个 cls参数。
Employee.set_raise_amt(1.06)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print('__________________')
print(Employee.num_of_emps)

print(emp_1.num_of_emps)
print(emp_2.num_of_emps)

print('_______________________')
new_emp_3 = Employee.from_string('Rebecca-hu-20000')

print(new_emp_3.fullname())

print('_______________________')

import datetime
my_date= datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))