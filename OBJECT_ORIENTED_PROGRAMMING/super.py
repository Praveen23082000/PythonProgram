
class Animals:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def __str__(self):
        return self.sound

class Lion(Animals):
    def __init__(self,name,sound):
        super().__init__(name,sound)
    def lion_power(self):
        print("hunting","running speed")

class Cat(Animals): 
    def __init__(self,name,sound):
        super().__init__(name,sound)
    def cat_power(self):
        print("running speed","night walking","hunting")

lion_substance=Lion("lion","ger")
lion_substance.lion_power()
print(lion_substance)

cat_substance=Cat("cat","meaw")
cat_substance.cat_power()
print(cat_substance)