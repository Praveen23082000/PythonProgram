
arr=[1,3,5,7,9,11,13]

print(arr)
ind=int(input("Enter the index:"))
if ind>=0 or ind<len(arr):
    ele=arr.pop(ind)
    print("Removed element :",ele)
    print(arr)
else:
    print("Index does not exist")