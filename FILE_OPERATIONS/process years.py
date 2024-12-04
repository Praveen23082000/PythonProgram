year_path= "C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\years.txt"

century_path= "C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\century year.txt"
leap_path= "C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\leap year.txt"

f_read=open(year_path,"r")
f_century_year=open(century_path,"w")
f_leap_path=open(leap_path,"w")

def is_century(year):
     if year %100==0 :
        return True
     else:
        return False

def is_leap(year):
    if year %400==0 or year %4==0 and year %100!=0 :
        return True
    else:
        False

for year in f_read:
    year=int(year)
    if is_century(year):
        f_century_year.write(str(year)+"\n")
    if is_leap(year):
        f_leap_path.write(str(year)+"\n")

f_read.close()
f_leap_path.close()
f_century_year.close()