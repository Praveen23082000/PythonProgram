f_read=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\palandro reads.txt","r")
f_word=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\palandro words.txt","w")

for line in f_read:
    word=line.rstrip("\n")
    reverse_word=word[::-1]
    if word==reverse_word:
        f_word.write(word+"\n")

f_read.close()
f_word.close()