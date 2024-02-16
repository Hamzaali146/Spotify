from typing import Any


class Person:
    def __init__(self,name,gender) -> None:
        self.name = name
        self.gender = gender
    def get_name(self):
        return self.name
    def get_gender(self):
        return self.gender
    def set_name(self,x):
        self.name = x
    def set_gender(self,y):
        self.gender = y
        
class Employee(Person):
    def __init__(self, name, gender,employee_id) -> None:
        super().__init__(name, gender)
        self.employeeid = employee_id
# a= Employee("sanya","female",22105)
# print(a.get_name())
# print(a.get_gender())
# a.set_gender("hamza")
# print(a.get_gender())
# print(a.pyaar())