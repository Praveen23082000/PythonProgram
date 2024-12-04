
# arr=[100,200,300,400,500,600,700]
# odd_position_number=[]
# for i in range(0,len(arr)):
#     if i%2!=0:
#         odd_position_number.append(arr[i])
# print(odd_position_number)

# odd_position_number=[arr[i] for i in range (0,len(arr)) if i%2!=0]
# print(odd_position_number)

#
arr=[100,200,300,400,500,600,700,800]
#     0   1   2   3   4   5   6   7
left=1
right=len(arr)-1
if right%2==0:
    right-=1
while(left<right):
    arr[left],arr[right]=arr[right],arr[left]
    left+=2
    right-=2
print(arr)
  
