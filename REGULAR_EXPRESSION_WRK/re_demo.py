from re import finditer

text="fatacftatbgdtabatstahjtat"

matches=finditer("at",text)

for obj in matches:
    print(obj.start(),obj.group())