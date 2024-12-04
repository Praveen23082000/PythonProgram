# sub calculation

def sub(num1,num2):
    result=num1-num2
    print(result)
sub(24,33)

# multiplication

def mul(num1,num2):
    result=num1*num2
    print(result)
mul(22,44)

# least digit remaining

def least_digit_max(num1,num2):
    num1_least_digit=num1%10
    num2_least_digit=num2%10
    print(num1 if num1_least_digit>num2_least_digit else num2)
least_digit_max(123,324)