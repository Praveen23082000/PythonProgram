

height=int(input("enter height cm  "))
weight=int(input("enter weight kg  "))
age=int(input("enter age  "))
gender=input("enter gender ").lower()

print(height,weight,age,gender)
"""
The basal Metabolic Rate (BMR)=

10*weight (kg)+ 6.25* height (cm)-5* age (y)+ 5 for (male)
10*weight (kg)+ 6.25* height (cm)-5* age (y)- 161 for (female)
"""

if gender=="male":
    BMR=10*weight+6.25*height-5*age+5
   
elif gender=="female":
    BMR=10*weight+6.25*height-5*age-161

else :
    print("""error""")

print(BMR)

activity_level=int(input)("""enter activity level
 press 1 for
 press 2 for
 press 3 for
 press 4 for
 press 5 for""")
