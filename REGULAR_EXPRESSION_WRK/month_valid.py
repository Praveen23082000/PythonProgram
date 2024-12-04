from re import fullmatch

month_count=input("enter month:>")

pattern="([1-9]|0[1-9]|1[0-2])"

matchers=fullmatch(pattern,month_count)

if matchers == None:
    print("invalid")
else:
    print("valid")
    