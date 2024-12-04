
class GrandParent:
    def m1(self):
        print("grand parent class m1 methods")

class Parent:
    def m2(self):
        print("parent class m2 methods")

class Child(Parent,GrandParent):
    def m3(self):
        print("child class m3 methods")

child_instance=Child()
child_instance.m1()
child_instance.m2()
child_instance.m3()



