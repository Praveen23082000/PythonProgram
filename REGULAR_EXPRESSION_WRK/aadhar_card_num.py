from re import fullmatch

aadhar_number=input("enter aadhar number:>")
pattern="[0-9]{12}"
matches=fullmatch(pattern,aadhar_number)

if matches == None:
    print("invalid")
else:
    print("valid")