from re import fullmatch

f=open("C:\\Users\\praveen\\Desktop\\python\\REGULAR_EXP_FILE_WORK\\phone_numbers.txt")

for num in f:
    phone=num.rstrip("\n")
    pattern="(91)?[0-9]{10}"
    matchers=fullmatch(pattern,phone)
    if matchers != None:
        print(phone)