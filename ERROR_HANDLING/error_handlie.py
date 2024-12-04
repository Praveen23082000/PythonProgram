num1=int(input("enter number1>"))
num2=int(input("enter number2>"))

try:
    result=num1/num2
    print(result)
except:
    print("error")

print("file write")
print("database")

#

arr=[1,2,3,4,5,6]
index=int(input("enter index position>"))

try:
    print(arr[index])
except:
    print("error")
print("file operation")
print("database")



num1=int(input("enter number1>"))
num2=int(input("enter number2>"))

try:
    result=num1/num2
    print(result)
except:
    num2=int(input("enter number2>"))
    result=num1/num2
    print(result)
finally:
    print("file operation")
    print("database commit") 



arr=[1,2,3,4,5,6,7]
index=int(input("enter index operations: "))

try:
    print(arr[index])
except Exception as e:
    print(e)

finally:
    print("high")

#

def review (rating):
    if rating<0:
        raise Exception("too low")
    else:
        print("done")
try:
    review(-2)
except Exception as e:
    print(e)
print("hai")
print("hello")



def review (rating):
    if rating<0:
        raise Exception("too low")
    elif rating>10:
        raise Exception("too high")
    else:
        print("done")
try:
    review(-2)
except Exception as e:
    print(e)
print("hai")
print("hello")

#

def poll(age):
    assert age>18, "invalid age"
    print("voted")
try:
    poll(12)
except Exception as p:
    print(p)

#

def is_leap_year(year):
    if year<0:
        return False
    if year % 400 == 0 or year % 4 == 0 and year % 100 !=0:
        return True
    else:
        return False

def test_is_leap_year():
    assert is_leap_year(2024)==True,"non century year check failed"
    assert is_leap_year(2025)==False,"invalid century check failed"
    assert is_leap_year(2000)==True,"century leap year check failed"
    assert is_leap_year(1900)==False,"invalid century year check failed"
    assert is_leap_year(-2024)==False,"invalid check year"
try:
    test_is_leap_year()
    print("test case passed")

except Exception as p:
    print(p)

#


