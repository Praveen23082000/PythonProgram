from re import findall
f=open("C:\\Users\\praveen\\Desktop\\python\\REGULAR_EXP_FILE_WORK\\dates.txt")
content=f.read()
pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"
dates=findall(pattern,content)
for date in dates:
    print(date)
f.close()
