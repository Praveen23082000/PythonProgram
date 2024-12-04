def number_dec(functions):
    def wrapper(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return functions(num1,num2)
    return wrapper
@number_dec
def sub_number(num1,num2):
    return num1-num2
@number_dec
def add_number(num1,num2):
    return num1+num2
@number_dec
def div_number(num1,num2):
    return num1/num2
    
print(sub_number(2,10))
print(add_number(2,10))
print(div_number(2,10))