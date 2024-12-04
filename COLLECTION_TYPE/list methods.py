
expenses=[12000,14000,20000,10000]
#           0     1     2      3
expenses[2]=22000

print(expenses)

# #
expenses=[12000,14000,20000,10000]

for exp in expenses:

    print(exp)

# sum methods

expenses=[12000,14000,20000,10000]

total=0

for exp in expenses:

    total+=exp

print(total)

# maximum value

expenses=[12000,14000,20000,10000]

maximum=0

for exp in expenses:

    if exp>maximum:

        maximum=exp

print(maximum)
    
# minimum value

expenses=[10000,12000,12000,12000,12000,10000]
min_exp=expenses[0]
for exp in expenses:
    if exp <min_exp:
        min_exp=exp
print(min_exp)