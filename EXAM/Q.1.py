# count of alphabets
from re import finditer

text="on june 5th,2024, we will celebrate @ our annual event: 'tech innovations 2024!'"

pattern="[a-zA-Z0-9]"


matchers=finditer(pattern,text)

for count in matchers:
    print(count.start(),count.group())
