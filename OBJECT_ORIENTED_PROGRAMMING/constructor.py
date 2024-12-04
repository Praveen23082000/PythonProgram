# initialize instance variable



class Mobile:
    model:str
    price:int
    brand:str
    def __init__(self,model,price,brand):
        self.model=model
        self.price=price
        self.brand=brand
    def display(self):
        print(self.model,self.price,self.brand)
Mobile1=Mobile("oneplus13",75000,"oneplus")
Mobile2=Mobile("iphone 16",130000,"apple")
Mobile1.display()
Mobile2.display()

