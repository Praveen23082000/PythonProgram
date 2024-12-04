
arr=[1,2,
[10,20],
[1,2,5,[10,3]]
,100]

list_object=[]
for item in arr:
    if isinstance(item,list):
        list_object.append(item)
print(list_object)
print(max(list_object,key=len))