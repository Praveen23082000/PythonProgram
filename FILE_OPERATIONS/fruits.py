fruits=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\fruits.txt")
product=[]
for f in fruits:
    product.append(f.rstrip("\n"))
print(product)

