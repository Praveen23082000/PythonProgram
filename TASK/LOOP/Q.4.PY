
arr=[3,3,3,5,6,7,7,1,9,2]

arr.sort()

arr1=[]

for num in arr:
    if num not in arr1:
        print(f"{num} : {arr.count(num)}")
        arr1.append(num)