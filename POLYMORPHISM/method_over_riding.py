
class Parent:
    def mobile(self):
        print("samsung")

class Child(Parent):
    def mobile(self):
        print("iphone")

child_instance=Child()
child_instance.mobile()

#

class Shipping:
    def calculate_shipping_coast(self,weight):
        print(weight*5)

class ExpressShipping(Shipping):
    def calculate_shipping_coast(self,weight):
        print(weight*20)

class StandardShipping(Shipping):
    def calculate_shipping_coast(self,weight):
        print(weight*10)

expe_instance=ExpressShipping()
expe_instance.calculate_shipping_coast(20)

std_instance=StandardShipping()
std_instance.calculate_shipping_coast(10)

