from re import fullmatch

year=input("enter year>")

pattern="((18|19)[0-9]{2}|20[01][0-9]202[0-4])"

matchers=fullmatch(pattern,year)

if matchers == None:
    print("invalid")
else:
    print("valid")
