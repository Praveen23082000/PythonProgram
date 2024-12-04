from re import finditer,findall

text="I have 3 cars,2 bikes and 1 cycle"
#pattern methods example

# pattern="[a-z]" #check for all lowercase alphabets
# # pattern="[0,9]"# check for digits
# # pattern="[a-zA-Z0,9]"# check for all alphanumerics
# pattern="[^ak]" # exclude(remove a,k letters) a,k
# pattern="[a-zA-Z0-9, ]"
pattern="[^a-zA-Z0-9]" #special characters

matches=finditer(pattern,text)

for obj in matches:
    print(obj.start(),"==>",obj.group())

