from re import fullmatch

number=input("enter number: ")

pattern="(KL)[0-9]{2}[A-Z](1,2)[0-9]{4}"

matches=fullmatch(pattern,number)

if matches == None:
    print("invalid")
else:
    print("valid")