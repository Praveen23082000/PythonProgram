f=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\years.txt","w")

for year in range(2000,2025):
    f.write(str(year)+"\n")
f.close()