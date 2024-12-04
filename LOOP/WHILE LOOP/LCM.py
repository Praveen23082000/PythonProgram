# find LCM of a number

number1=int(input("enter number1: "))
number2=int(input("enter number2: ")) 

if(number1>number2):
    maximum_num=number1
else:
    maximum_num=number2
lcm=maximum_num
while(lcm%number1 !=0) or (lcm%number2 !=0):
    lcm=lcm+maximum_num
print(lcm)
 
gcd=(number1*number2//lcm)
print(gcd)