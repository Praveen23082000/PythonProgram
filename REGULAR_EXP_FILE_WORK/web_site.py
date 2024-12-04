from re import findall

f=open("C:\\Users\\praveen\\Desktop\\python\\REGULAR_EXP_FILE_WORK\\web_site.txt")

content=f.read()
pattern="https?://[\w\S]+"
urls=findall(pattern,content)

for url in urls:
    print(url)