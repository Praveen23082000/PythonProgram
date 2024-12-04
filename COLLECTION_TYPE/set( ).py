
# st=set()#set

# st={10,20,30,}

# st={"red,blue"}
# print(st)

# # add
# st.add("black")
# print(st)

# arr=[10,20,30,10,40,20]

# st=set()

# for num in arr:
#     st.add(num)
# print(st)

# st1={1,2,3}
# st2={3,4,5,6,7}

# intersection_set=st1.intersection(st2)
# print(intersection_set)

# # union
# union_set=st1.union(st2)
# print(union_set)

# # difference
# different_set=st1.difference(st2)
# print(different_set)

# # remove
# st1.remove(3)
# print(st1)

# users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]
# rahul_followers=["rohit","kohli","rishab","rahul"]
# sanju_followers=["sanju","rohit","kohli"]

# user_set=set(users)
# rahul_followers_set=set(rahul_followers)
# sanju_followers_set=set(sanju_followers)

# for_suggestion=user_set.difference(rahul_followers_set)
# print(for_suggestion)

# mutual = rahul_followers_set.intersection(sanju_followers_set)
# print(mutual)


# st1={1,2,3}
# st2={4,5,1,2}

# # # issubset
# print(st1.issubset(st2))

# # # symmetrics
# symmetrics_difference=st1.symmetric_difference(st2)
# print(symmetrics_difference)

# # # update
# st1.update(st2)
# print(st1)

# # clear
# st1.clear()
# print(st1)

# # discard
# st1.discard(2)
# print(st1)

text="this is a test to remove duplicate words this test is simple"
text="this simple test remove duplicate words"

words=text.split(" ")
print(set(words))
words2=text.split(" ")
print(set(words).issubset(set(words2)))
