


# def add_number (*args):
#     print(args)

# add_number(10,20)
# add_number(10,20,30)

# #

# def second_max_num (*numbers):
#     num=sorted(numbers)
#     print(num[-2])
# second_max_num(10,20,30,40)
# second_max_num(10,20,8,40,9,5)

#

# def calculator (*num,**number):
#     if number.get("operation")=="+":
#         return sum(num)

#     if number.get("operation")=="*":
#         result=1
#         for data in num:
#             result=result*data
#         return result

# print(calculator(10,20,30,40,operation="+"))
# print(calculator(10,20,30,40,operation="*"))

#

# def student_info (*args,**kwargs):
#     if kwargs.get("operation")=="avg":
#         return sum(args)/len(args)
#     if kwargs.get("operation")=="total":
#         return sum(args)

# print(student_info(45,43,44,operation="avg"))
# print(student_info(45,43,44,operation="total"))

# #

def sort_numbers (*args,**kwargs):
    if kwargs.get("reverse")=="true":
        return sorted(args,reverse= True)
        
    if kwargs.get("reverse")=="false":
        return sorted(args)

print(sort_numbers(1,2,6,4,15,11,reverse="true"))
print(sort_numbers(1,2,6,4,15,11,reverse="false"))