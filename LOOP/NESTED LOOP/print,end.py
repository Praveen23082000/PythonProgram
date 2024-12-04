
# good $$ afternoon  all

print("good",end="$$")

print("afternoon",end="\t")

print("all")

# row=7

# colum=5

for row in range(1,8):
 
    for col in range(1,6):

        print("*",end="\t")

    print()

# $
# $ $
# $ $ $
# $ $ $ $
# $ $ $ $ $
# $ $ $ $ $ $

for row in range(1,7):
    for col in range(1,row+1):
        print("$",end="\t")
        row=row+1
    print()


# $
# $ $
# $ $ $
# $ $ $ $
# $ $ $ $ $
# $ $ $ $ $ $

for row in range(1,7):
    for col in range(1,row+1):
        print("$",end="\t")
      
    print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for row in range(1,6):
    for col in range(1,row+1):
        print(row,end="\t")
    print()
    
# * * * * *
# * * * *
# * * *
# * *
# *

for row in range(5,0,-1):
    for col in range(1,row+1):
        print("*",end="\t")
    print() 
    
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 5
# 0 1 2 3 5 8

           