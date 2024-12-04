from re import finditer

text="abbababababbabababbaaa"

# pattern="a{2}"
# pattern="b{2}"
# pattern="a{1,3}" # minimum1 maximum3  


matchers=finditer(pattern,text)

for obj in matchers:
    print(obj.start(),"==>",obj.group())