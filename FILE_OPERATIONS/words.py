f=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\words.txt")
words=[]
for line in f:
    line=line.rstrip("\n")
    all_words=line.split(" ")
    for w in all_words:
        words.append(w)
print(words)

word_counts={word:words.count(word) for word in words}
print(word_counts) 

nested_word_count=[[v,k] for k,v in word_counts.items()]
print(sorted(nested_word_count,reverse=True))