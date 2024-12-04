
student_date={
             "hari":{45,40,35},
             "vipin":{34,40,35},
             "vinay":{45,40,35},
             "bijoy":{33,38,35},
             "anvin":{32,30,40}
}
# for i,element in enumerate(student_date):
#     print(i,element)

index=2
for i,element in enumerate( student_date):
    if i+1==index:
       print(element)
       
# avg marks print
student_avg_marks={k:sum(v)/len(v) for k,v in student_date.items()}
print(student_avg_marks)


source_word="CHICKEN"
target_word="HEN"

is_present=True
for ch in source_word:
    if ch  in target_word:
        if source_word.count(ch)==target_word.count(ch):
            is_present=False
        else:
            is_present=False
print("kangaroo" if is_present==True else "no")


source_word="CHICKEN"
target_word="HEN"

# character_count={}
# for ch in source_word:
#     if ch in character_count:
#         character_count[ch]+=1
#     else:
#         character_count[ch]=1
# print(character_count)

character_count={ch:source_word.count(ch)  for ch in source_word}
is_kangaroo=True
for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]-=1
    else:
        is_kangaroo=False
        break
print(is_kangaroo)

#

user_input=input("enter bracket pairs")
symbol_dictionary={"(" : ")",
                   "[" : "]",
                   "{" : "}"}
symbol_stack=[]

top=-1

is_valid=True

for symbol in user_input:
    if symbol in symbol_dictionary:#symbol is an opening
        is_valid==False
        break
    
    elif symbol == symbol_dictionary.get(symbol_stack[top]):
        top=top+1
        symbol_stack.append(symbol)
    
    elif symbol == symbol_dictionary.get(symbol_stack[top]):
        top=top-1
        symbol_stack.pop()

    else:
        is_valid=False
    
    if len(symbol_stack)==0 and is_valid:
        print("valid")

    else:
        print("invalid")
