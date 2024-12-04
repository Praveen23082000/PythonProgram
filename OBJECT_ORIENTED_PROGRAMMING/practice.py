class Phones:
    def __init__(self,brand,price,model):
        self.brand=brand
        self.price=price
        self.model=model
    def display(self):
        print(self.brand,self.price,self.model)
first_phones=Phones("apple",130000,"iphone 16")
first_phones.display()
