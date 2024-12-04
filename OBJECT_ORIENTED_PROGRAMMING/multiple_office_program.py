
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person_info(self):
        print(self.name,self.age)

class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
    def display_employee(self):
        print(self.emp_id,self.salary)

class Manager(Person,Employee):
    def __init__(self,name,age,emp_id,salary,department):
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.department=department
    def display_manger_info(self):
        self.display_person_info()
        self.display_employee()
        print(self.department)

manager_instance=Manager("Praveen",24,277,50000,"HR")
manager_instance.display_manger_info()