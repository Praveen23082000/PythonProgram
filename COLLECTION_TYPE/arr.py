arr=[10,20,30,40]
#     0  1  2  3

for i in range(0,len(arr)):

    print(arr[i])

# a print even number

arr=[1,2,4,5,6,7,8,9,10,11]

for i in range(0,len(arr)):

    if arr[i]%2==0:

        print(arr[i])

#

arr=[2,3,4,5]
#    0 1 2 3 
sum=int(input("enter sum"))
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        cur_sum=arr[i]+arr[j]
        if sum==cur_sum:
            print(arr[i],arr[j])
            break 


lst=[1,2,3,4,5,7]

left=0
right=len(arr)-1
while (left<right):
    curr_sum=arr[left]+arr[right]
    if curr_sum==sum:
        print(arr[left],arr[right])
        break
    elif cur_sum>sum:
        right=right-1
    elif cur_sum<sum:
        right=right+1
        
