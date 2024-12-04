
start=int(input("enter start:  "))
end=int(input("enter limit:  "))

if start<end:
    for run in range(start,end+1,1):
        print(run)
else:
    for run in range(start,end-1,1):
        print(run)

    start=int(input("enter start: "))
end=int(input("enter limit: "))

if start<end:

    for num in range(start,end+1,1):

        print(num)

else:

    for num in range(start,end-1,1):
        print(num)
