
cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]
# print count of vehicles
print(f"total vehicles:{len(cars)}")

# print available color of baleno
baleno_colours=[c.get("colors") for c in cars if c.get("name")=="baleno"]
print(baleno_colours[0])

# print all brands
all_brands={car.get("brand")for car in cars}
print(all_brands)

# print car name available in amt transmission
available_amt_car=[car.get("name")for car in cars if "amt" in car.get("transmissions")]
print(available_amt_car)

# cars available in blue color
available_color=[car.get("name") for car in cars if "blue" in car.get("colors") ]
print(available_color)

# print all transmission
transmission={tra for car in cars for tra in car.get("transmissions")}
print(transmission)

# print all colors
all_color={ co for car in cars for co in car.get("colors")}
print(all_color)

# most popular color
colour=[color for car in cars for color in car.get("colors")]
print(colour)

count={color:colour.count(color) for color in colour}
print(count)

popular_color=max(count,key=lambda c:count.get(c))
print(popular_color)

# costly car
costly_car=max(cars,key=lambda c:c.get("price"))
print(costly_car.get("name"))

# car with minimum cost cars
low_cost=min(cars,key=lambda p:p.get("price"))
print(low_cost.get("name"))

# sort with car price
sort_with_car=sorted(cars,key=lambda p:p.get("price"))
sort_list={p.get("name") : p.get("price") for p in sort_with_car}
print(sort_list)
