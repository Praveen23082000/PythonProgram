# # # Q.1
# # name={"appu":10,"manu":12,"ponnu":8,"ammu":5,"achu":14}
# # print(name.get("ponnu"))

# # # Q.2
# # name1={"appu":10,"manu":12,"ponnu":8}
# # name2={"ammu":5,"achu":14,"chikku":3}
# # name1.update(name2)
# # print(name1)

# # Q.3
# marks={"appu":48,"manu":51,"ponnu":20,"ammu":20,"achu":55}
# value=marks.values()
# total=sum(value)
# avarage=total/len(marks)
# print(avarage)

# # Q.4
# arr=[1,2,3,4,5,6,7,8,9,10]
# square={num:num**2 for num in arr}
# print(square)
# # square_number={}
# # for num in arr:
# #     square_number[num]=num**2
# # print(square_number)

# Q.5
name=["praveen","rahul","ajay","navya"]
age=[25,23,24,21]
details={name[i]:age[i] for i in range(len(name))}
print(details)

