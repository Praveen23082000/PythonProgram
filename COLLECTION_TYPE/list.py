# end object use ...APPEND...

colors=["red","green","blue"]

# insert new object end of the list

colors.append("yellow")
print(colors)

# colors.pop()remove the object from list and returns it

colors=["red","green","blue"]

colors.pop()
print(colors)

# remove object green

colors=["red","green","blue"]
     #   0      1       2
colors.pop(1)
print(colors)

# insert

colors=["red","green","blue"]

colors.insert(0,"pink")
print(colors)

# copy methods

praveen_fav_colors=["red","blue","black","white"]

navya_fav_colors=praveen_fav_colors.copy()
navya_fav_colors.pop()
print("navya",navya_fav_colors)
print("praveen",praveen_fav_colors)

# sort

lst=[2,6,4,8,7,5]

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

#

arr1=[10,13,8,11,20]
arr2=[2,20,7,8,13]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
         print(arr1[i])

