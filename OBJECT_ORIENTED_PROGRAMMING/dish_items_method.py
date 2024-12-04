
class Cuisine:
    def __init__(self,cuisine_name):
        self.cuisine_name=cuisine_name
    def display_cuisine (self):
        print(self.cuisine_name)

class MealTypes:
    def __init__(self,name):
        self.name=name
    def display_meal (self):
        print(self.name)

class Dish(Cuisine,MealTypes):
    def __init__(self,cuisine_name,name,dish_name):
        Cuisine.__init__(self,cuisine_name)
        MealTypes.__init__(self,name)
        self.dish_name=dish_name
    def set_display(self):
        self.display_cuisine()
        self.display_meal()
        print(self.dish_name)
dish_instance=Dish("france","break fast","pasta")
dish_instance.set_display()  