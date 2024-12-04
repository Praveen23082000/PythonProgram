text="this is a simple question return word with maximum number of characters" 


words=text.split(" ")

def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)