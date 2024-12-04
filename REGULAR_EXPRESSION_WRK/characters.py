from re import finditer

text="I have 3 cars,2 bikes and 1-cycle"

# pattern=r"\w" # "[a-zA-Z0-9]"
# pattern="\d" # "[0-9]" digit counting
# pattern="\D" # "[^0-9]" digits excluding (remove digit)
# pattern="\W" # "[^a-zA-Z0-9]" special characters
# pattern="\s" # space
# pattern="\S" # exclude space (space remove)

matches=finditer(pattern,text)

for obj in matches:
    print(obj.start(),obj.group())

