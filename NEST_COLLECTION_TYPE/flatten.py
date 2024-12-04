
arr=[[10,20],
     [20,30],
     [30,40],
     [40,50]]

flat_list=[num for ls in arr for num in ls]
print(flat_list)

# gt 30
gt_num=[num for ls in arr for num in ls if num >30]
print(gt_num)
