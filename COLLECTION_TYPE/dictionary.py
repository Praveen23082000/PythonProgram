
# product={"id":"praveen","title":"car","price":700000,"brand":"hyundai","offer":10}

# print(product["price"])
# print(product["brand"])

# #update
# product["price"]=800000
# print(product)

# #adding
# product["place"]="ottappalam"
# print(product)

# # exist
# # not exist
# if "offer" in product:
#     product["offer"]=10
# else:
#     product["offer"]=20
# print(product)

# employee={"id":12000,"name":"praveen","salary":25000,"department":"developer","experience":2}

# print(employee["department"])

# # adding
# employee["contact"]=9061288026
# print(employee)

# if employee["experience"]>5:
#     employee["salary"]+=3000
# else:
#     employee["salary"]+=1000
# print(employee)

# if employee["experience"]>5:
#     employee["roll"]="sde"
# else:
#     employee["roll"]="jde"
# print(employee)

employee={"id":64,
"name":"praveen",
"salary":25000,
"department":"developer",
"age":24}
#get
print(employee.get("salary"))

#pop
employee.pop("salary")
print(employee)

# return all keys
for k in employee.keys():
    print(k)

# return all values
for v in employee.values():
    print(v)

# return keys and values both print in output
for k,v in employee.items():
    print(k,v)

