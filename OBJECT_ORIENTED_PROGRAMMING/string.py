class Car:
    def __init__(self,name,brand,fuel_type):
        self.name=name
        self.brand=brand
        self.fuel_type=fuel_type
    def display(self):
        print(self.name,self.brand,self.fuel_type)
    def __str__(self):
        return self.brand
car_substance1=Car("thar","mahindra","petrol")
car_substance1.display()
print(car_substance1)

#

class Editor:
    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor
    def display(self):
        print(self.name,self.vendor)
    def __str__(self):
        return self.name
editor_substance1=Editor("vs code","micro soft")
# editor_substance1.display()
print(editor_substance1)