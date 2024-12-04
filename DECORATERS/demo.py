
def swap_dec(function):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return function(n1,n2)
    return wrapper

@swap_dec
def smart_sub(num1,num2):

    return num1 - num2

@swap_dec
def smart_div(num1,num2):
    return num1 / num2

print(smart_sub(2,8))
print(smart_div(2,10))

#

def smart_dec(functions):
    def wrapper(n1,n2):
        if n1<n2:
            n1,n2=n2,n1
        return functions(n1,n2)
    return wrapper    
@ smart_dec
def smart_sub(num1,num2):
    return num1-num2
@ smart_dec
def smart_div(num1,num2):
    return num1/num2
@ smart_dec
def smart_mul(num1,num2):
    return num1*num2

print(smart_sub(8,2))
print(smart_div(2,10))
print(smart_mul(2,2))

