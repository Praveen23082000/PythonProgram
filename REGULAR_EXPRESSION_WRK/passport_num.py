from re import fullmatch

passport_num=input("enter passport number:>")
pattern="[A-Z]{1}[0-9]{7}"
matches=fullmatch(pattern,passport_num)

if matches == None:
    print("invalid")
else:
    print("valid")