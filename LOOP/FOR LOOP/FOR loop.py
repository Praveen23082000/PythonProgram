# program to print numbers from 1 to 10


sequence=range(1,11,1)


for num in sequence:

    print(num)


# program to print  numbers from 10 to 1


sequence=range(10,0,-1)


for num in sequence:

    print(num)


# program to print numbers 0 to 10


color_number=range(0,-1,-1)


for num in color_number:

    print(num)


# start to end


start=int(input("enter start: "))

end=int(input("enter limit: "))


sequence=range(start,end+1,1)


for num in sequence:

    print(num)


# reverse end to start running program



start=int(input("enter start: "))

end=int(input("enter limit: "))


if start<end:


    for num in range(start,end+1,1):

        print(num)


else:


    for num in range(start,end-1,1):
        print(num)



    