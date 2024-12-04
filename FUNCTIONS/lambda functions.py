
cube=lambda num:num**3
print(cube(12))

add=lambda num1,num2:num1+num2
print(add(20,30))

#
max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2       
print(max_two("mango","orange"))

#
min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2
print(min_two("mango","orange"))

#
smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(200,1300)) 

#
words=["hello","hai","morning","test","apple"]

def get_length(word):
    return len(word)
print(max(words,key=get_length))

#
def get_length(word):
    return len(word)
print(min(words,key=get_length))

#
print(max(words,key=lambda word:len(word)))

#
text="this is a simple programming question to find word with maximum number of characters"

words=text.split(" ")#split words
print(words)

def get_length(w):
    return len(w)
print(max(words,key=get_length))

#words sorting
words=text.split(" ") 

def get_length(word):
    return len(word)
start_word=sorted(words,key=get_length,reverse=True)
print(start_word)

#recursive word or most repeat words print
words=text.split(" ")

def get_count(word):
    return words.count(word)
print(max(words,key=get_count))

text="ABBBACCD"

def get_count(spell):
    return text.count(spell)
print(max(text,key=get_count))

#non not repeat spell
def get_count(spell):
    return text.count(spell)
print(min(text,key=get_count))