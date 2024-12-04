
from json import load
f=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\countries.json",encoding="utf-8")
data=load(f)

# print number of counties
# print(len(data))

# print all countries names
all_counties_name=[country.get("name") for country in data]
# print(all_counties_name)

# all regions
all_regions=[region.get("region") for region in data]
# print(set(all_regions))

# all regions counts
all_counts={ region:all_regions.count(region) for region in all_regions }
# print(all_counts)

# highest regions 
highest_regions=max(all_counts,key=lambda k:all_counts.get(k))
# print(highest_regions)

# capital of specific country
country_capital=[country.get("capital") for country in data if country.get("name")=="India"]
# print(country_capital)

# most number of borders
# country_border_count= {country.get("name"):len(country.get("borders",[]))for country in data }
# print(country_border_count)

max_borders_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
# print(max_borders_country)

# most population countries
most_country={country.get("name"):country.get("population")for country in data }
most_population=max(most_country,key=lambda k:most_country.get(k))
# print(most_country)

alpha_three_code=[country.get("borders") for country in data if country.get("name")=="India"][0]
for code in alpha_three_code:
    for country in data:
        if country.get("alpha3Code")==code:
            print(country.get("name")) 
