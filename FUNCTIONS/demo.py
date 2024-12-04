
# def factorial(num):

#     fact=1

#     for i in range(1,num+1):





def num_check(number):
    if number%2==0:
        return "even"
    else:
        return "odd"

print(num_check(10))

# create a function max_two with two parameter num1,num2 return large number

def max_two(num1,num2):

    return num1 if num1>num2 else num2

print(max_two(100,200))

# create a function  min_two with two parameter num1,num2 return smallest number

def min_two(num1,num2):

    return num1 if num1<num2 else num2

print(min_two(300,700))

# multiplication table(5,10)

def multiplication_table(number,n=20):

    for i in range(1,n+1):

        print(f"{i} * {number} = {i * number}")

multiplication_table(5)

# create a function exponent with two parameter num1,n

def expo(number,n=2):
    
    return number**n

print(expo(6))

# create a function smart_sub with twp parameter num1,num2,reverse

def smart_sub(num1,num2,reverse):

    return num2-num1 if reverse==True else num1-num2

print(smart_sub(10,30,True))

    
# create a function random_numbers(start,end,step)

def random_numbers(start,step,end):

    while(start>end):
        print(start)

        start=start+end

        break

random_numbers(100,200,2)
 
   


      


