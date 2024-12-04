from re import fullmatch

month_date=input("enter date:>")

pattern="(0?[1-9]|1[0-9]|2[0-9]|3[0-1])"

matchers=fullmatch(pattern,month_date)

if matchers == None:
    print("invalid")
else:
    print("valid")