from re import finditer

f=open("C:\\Users\\praveen\\Desktop\\python\\REGULAR_EXP_FILE_WORK\\#tag.txt")

for obj in f:
    words=obj.rstrip("/n")
    pattern="#[a-zA-Z]*"
    matchers=finditer(pattern,words)
    for p in matchers:
        print(p.group())
    