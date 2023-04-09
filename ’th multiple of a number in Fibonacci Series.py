num=int(input("enter the number: "))
nth=int(input("enter the value: "))
a=0
b=1
c=0
i=1
while i<=nth:
    c=a+b
    a=b
    b=c
    if c%num==0:
        print(f"{i} multiple of {num} is {c}")
        i+=1