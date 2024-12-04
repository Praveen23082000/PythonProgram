

class GrandParent:
    def m(self):
        print("grand parent class m1 methods")

class Parent:
    def m(self):
        print("parent class m2 methods")

class Child(Parent,GrandParent): # out put will be method from first class
    def m3(self):
        print("child class m3 methods")

child_instance=Child()
child_instance.m()

