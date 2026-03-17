from abc import ABC, abstractmethod

class Employee(ABC):
    contador = 0
    def __init__(self, First_name, Last_name):
        self.First_name = First_name
        self.Last_name = Last_name
        Employee.contador = Employee.contador + 1
    def get_First_name(self):
        return self.First_name
    def get_Last_name(self):
        return self.Last_name
    def set_First_name(self, new_fn):
        self.First_name = new_fn
    def set_Last_name(self, new_ln):
        self.Last_name = new_ln
    @abstractmethod
    def compute_salary(self):
        pass
    def full_name(self):
        return self.First_name + " " + self.Last_name
    @classmethod
    def get_contador(cls):
        return cls.contador

class Fulltime(Employee):
    def __init__(self, First_name, Last_name, base_salary = 0):
        super().__init__(First_name, Last_name)
        self.base_salary = base_salary
    def get_base_salary(self):
        return self.base_salary
    def set_base_salary(self, new_bs):
        self.base_salary = new_bs
    def compute_salary(self):
        vt = self.base_salary + 200
        return vt

class Hourly(Employee):
    def __init__(self, First_name, Last_name, work_h, value_h):
        super().__init__(First_name, Last_name)
        self.work_h = work_h
        self.value_h = value_h
    def get_work_h(self):
        return self.work_h
    def set_work_h(self, new_wh):
        self.work_h = new_wh
    def get_value_h(self):
        return self.value_h
    def set_value_h(self, new_vh):
        self.value_h = new_vh
    def compute_salary(self):
        vth = self.work_h * self.value_h
        return vth