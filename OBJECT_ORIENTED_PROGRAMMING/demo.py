# class student:
#     name:str
#     age:int
#     contact:int
#     course:str
#     def set_student(self,name,age,contact,course):
#         self.name=name
#         self.age=age
#         self.contact=contact
#         self.course=course
#     def set_display(self):
#         print(self.name,self.age,self.contact,self.course)

# names=student()
# names.set_student("praveen",24,9061288026,"python")
# names.set_display()



class Student:
    def __init__(self,name,course,roll_number):
        self.name=name
        self.course=course
        self.roll_number=roll_number
    def set_display(self):
        print(self.name,self.course,self.roll_number)
names=Student("praveen","python",64)
names.set_display()

