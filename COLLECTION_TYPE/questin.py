
arr=[10,20,30,40,2,3]

square_num={}
for num in arr:
        square_num[num]=num**2
for k,v in square_num.items():
    print(k,":",v)

arr=[10,20,30,40,2,3]

cube_num={num:num**3 for num in arr}
print(cube_num)

# odd square an even cubes return
arr=[10,20,30,40,2,3]

even_square={num:num**2 for num in arr if num%2==0}
print(odd_square)

odd_cubes={num:num**3 for num in arr if num%2!=0}
print(even_cubes)

# frequency counts

arr=[10,20,30,40,10,30,2,3,4,5,20]

frequency_count={num:arr.count(num) for num in arr}
print(frequency_count)

#
text="ABBACCDRTC"

character_frequency={ch:text.count(ch) for ch in text}
print(character_frequency)

# non recursive methods

character_frequency={ch:text.count(ch) for ch in text if text.count(ch) == 1}
print(character_frequency)

# for k,v in character_frequency.items():
#     if v==1:
#         print(k)

non_frequency_character={k for k,v in character_frequency.items() if v==1}
print(non_frequency_character)

words=["hello","hai","hello","hello","this","is","hai","this"]

word_frequency={w:words.count(w) for w in words}
print(word_frequency)

recursive_words=[k for k,v in word_frequency.items() if v>1]
print(recursive_words)

