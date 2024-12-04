

begin=int(input("enter start "))
end=int(input("enter end "))

reverse=True if begin>end else False

print(reverse)

i=begin

while(i<=end if reverse==False else i>=end):

    if i%2==0:

        print(i)

    if reverse==False:
 
        i=i+1

    else:

        i=i-1
