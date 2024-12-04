p=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\results dtls.txt")
f=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\fail students.txt")
all_students=set()
failed=set()
for line in p:
    line=line.rstrip("\n")
    all_students.add(line)

for line in f:
    line=line.rstrip("\n")
    failed.add(line)

passed_students=all_students.difference(failed)
print(passed_students)