from re import fullmatch

mobile_number=input("enter mobile number:")

pattern="(91)?[0-9]{10}"

matchers=fullmatch(pattern,mobile_number)

if matchers == None:
    print("invalid")
else:
    print("valid")