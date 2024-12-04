from re import fullmatch

gmail_valid=input("enter valid>")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

matchers=fullmatch(pattern,gmail_valid)

if matchers == None:
    print("invalid")
else:
    print("valid")