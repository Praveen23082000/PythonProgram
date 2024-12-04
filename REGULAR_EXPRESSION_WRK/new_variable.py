from re import fullmatch

user_input=input("enter variable name> ")

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matchers=fullmatch(pattern,user_input)

if matchers == None:
    print("invalid")
else:
    print("valid")