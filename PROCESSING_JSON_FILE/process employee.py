from json import load
f=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\{ }employee.json")
data=load(f)

for emp in data:
    print(emp)
