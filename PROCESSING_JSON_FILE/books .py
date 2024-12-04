from json import load
f=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\books.json")
data=load(f)

for book in data:
    print(book)

# TITLE
all_title=[book.get("title") for book in data]
print(all_title)

# BOOKS WITH PAGES < 250
page_filter=[book.get("title") for book in data if book.get("pages") < 250]
print(page_filter)

# PRINT ALL GENRES
all_genres={book.get("genre") for book in data}
print(all_genres)

# COSTLY BOOKS
costly_books=max(data,key=lambda book:book.get("price"))
print(costly_books)

# AUTHOR WITH MORE THAN BOOK
all_author=[book.get("author") for book in data]
author_count={ac:all_author.count(ac)for ac in all_author}
print([k for k,v in author_count.items() if v>1])
