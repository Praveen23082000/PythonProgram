
products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
     {"id":6,"title":"iphone16proplus","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles

# print mobile titles

# print samsung mobiles

print(len(products))

#
for m in products:
    print(m.get("title"))

#
for product in products:
    if product.get("brand")=="samsung":
        print(product)

# maximum costly products print

costly_mobile=max(products,key=lambda product:product.get("price") )
print(costly_mobile)

# all collect costly mobiles

costly_price_mobile=max(products,key=lambda product:product.get("price"))
max_price=costly_price_mobile.get("price")
costly_mobile_price=[product.get("title")for product in products if product.get("price")==max_price]
print(costly_mobile_price)

# samsung mobiles counts

for product in products:
    if product.get("brand")=="samsung":
        print(product)
print(len(product)) 

#
all_brands=[p.get("brand") for p in products ]
print(all_brands)

brand_counts={b:all_brands.count(b) for b in all_brands}
print(brand_counts)

#
movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vaazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]
# TOTAL NUMBER OF MOVIES
print(len(movies))

# PRINT MOVIE TITLES
for m in movies:
    print(m.get("title"))

# PRINT VAAZHA MOVIE
for m in movies:
    if m.get("title")=="vaazha":
        print(m)

# MAXIMUM RUN TIME
max_run_movie=max(movies,key=lambda m:m.get("run_time"))
print(max_run_movie)

