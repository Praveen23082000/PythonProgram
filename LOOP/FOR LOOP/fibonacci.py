
prev=0
curr=1

print(prev)
print(curr)

for i in range(1,5):

    next=prev+curr
    print(next)
    prev=curr
    curr=next


# is 51 fibonacci number?

number=int(input("enter number "))

prev=0
curr=1

is_fibo=False

for i in range(1,number+1):

    next=prev+curr
    prev=curr
    curr=next

    if next==number:
        is_fibo=True
        
print(is_fibo)


number=int(input("enter number:"))
prev=0
curr=1
is_fibo=False
for i in range(1,number+1):
    next=prev+curr
    prev=curr
    curr=next
    if next==number:
        is_fibo=True
print(is_fibo)
        











number=int(input("enter number"))
prev=0
curr=1
is_fibo=True
for i in range(1,number+1):
    next=prev+curr
    prev=curr
    curr=next
    if next==number:
        is_fibo=False
print(is_fibo)