text = "this is a simple python program that print most recursive word . this program is simple"
lst=text.split()

frequent_word={x:lst.count(x) for x in lst}
most_frequent=max(frequent_word.items(),key=len)
print(most_frequent)