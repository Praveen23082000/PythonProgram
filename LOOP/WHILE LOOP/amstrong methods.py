# amstrong methods

# number=input("enter number ")

# digit_count=len(number)

# print(digit_count)

number=int(input("enter number: "))

original=number

digit_count=len(str(number))

total=0

while(number!=0):

    digit=number%10
    exponent=digit**digit_count
    total=total+exponent
    number=number//10

print("amstrong number"if total==original else "not amstrong ")