
arr=[2,3,4,5,6,7]

# # square method

square=[num**2 for num in arr]
print(square)


# # even method

even_number=[num for num in arr if num%2==0]
print(even_number)

# # odd method

odd_number=[num for num in arr if num%2!=0]
print(odd_number)

# # >5 method

gt_five=[num for num in arr if num>5]
print(gt_five)

# #

text=["apple","banana","orange","carrot"]

name=[ name for name in text if name[0] in "aeiou"]
print(name)

# #

consonant_words=[w for w in text if w[0] not in "aeiou"]
print(consonant_words)

# longest word

long=max([len (w) for w in text])
longest_word=[w for w in text if len(w)==long]
print(longest_word) 

