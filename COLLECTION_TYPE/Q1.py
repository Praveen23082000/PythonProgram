
# arr=[100,200,300,400,500]
# k=1
# for i in range(1,k+1):
#     popped_element=arr.pop()
#     arr.insert(0,popped_element)
# print(arr)

# #
# arr1=[10,12,11,14,15,16]
# arr2=[20,21,10,14,13,12]

# arr1.sort()
# arr2.sort()

# p1=0
# p2=0

# while(p1<len(arr1) and p2<len(arr2)):
#     if arr1[p1]==arr2[p2]:
#         print(arr1[p1])
#         p1+=1
#         p2+=1
#     elif arr1[p1]<arr2[p2]:
#         p1+=1
#     elif arr1[p1]>arr2[p2]:
#         p2+=1
# #
# arr=[1,2,4,6,7]

# arr.sort()

# for i in range(0,len(arr)-1):
#     j=i+1
#     result=arr[j]-arr[i]
#     if result!=1:
#         print(arr[i]+1)
#         break

# #duplicate numbers

# arr=[1,2,2,2,1,4,5]

# arr.sort()

# duplicate_number=[]

# for i in range(0,len(arr)-1):
#     j=i+1
#     result=arr[j]-arr[i]
#     if result==0:
#         if arr[i] not in duplicate_number:
#             duplicate_number.append(arr[i])
# print(duplicate_number)
        
#
lst1=["apple","mango","onion","potattoo"]
lst2=[100,200]

result={}
for x in range(0,len(lst2)):
    list_one_index_element=lst1[x]
    list_two_index_element=lst2[x]
    result[list_one_index_element]=list_two_index_element

balance_element=lst1[len(lst2):]
for index,element in enumerate(balance_element):
    result[element]=index+1
print(result)