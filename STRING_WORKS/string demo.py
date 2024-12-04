

text="helloworld"


# capitalize()


print(text.capitalize())


# casefold()


print(text.casefold())

# isalpha()

print(text.isalpha())


# isdigit()


print(text.isdigit())


# isalnum()


print(text.isalnum())

# startswith(str)

print(text.startswith("he"))

# endswith(str)

print(text.endswith("ld"))

# characters picking in helloworld

for word in text:
    print(word)

# split()

text="hello world python"

words=text.split(",")

print(words)

# strip()

text="this \n is \n car \s"

new_word=text.strip("\n,\n,\s")

print(new_word)

# replace() any words in text

text="hello world program" 

new_word=text.replace("o","p")

print(new_word)

# words  slicing methods

text="python programming"
  #   012345 67890123456  
#   string_object=(start:end:step)

print(text[0:6])

print(text[: :-1])

print(text[:7])

print(text[:17])

# reverse text 

# text=input("enter text:")

# reverse_text=text[::-1]

# if text==reverse_text:
#     print("palindrome")

# else:
#     print("not palindrome")

# next reverse methods

text="hello"

lenght=len(text)-1

reverse_string=""

for i in range(lenght,-1,-1):

    reverse_string+=text[i]

print(reverse_string)

# index method

print(text.index("o"))

print(text.index("l"))


text="hellopython"
#ollehpython

o_index=text.index("o")

reversed_sub_str=text[o_index-1::-1]

balance_sub_str=text[o_index:]

result=reversed_sub_str+balance_sub_str

print(result)

#

text1="pqr"
text2="rst"

result=""

for i in range(0,len(text1)):

    result+=text1[i]+text2[i]

print(result)

#

text1="pqrst"
text2="abc"

smallest_text=text1 if len(text1) < len(text2) else text2

largest_text=text1 if len(text1) > len(text2) else text2

result=""

for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]

balance_text=largest_text[len(smallest_text):]

result+=balance_text

print(result)


