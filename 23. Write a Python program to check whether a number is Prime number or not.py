num=int(input("enter the number: "))
li=[]
for i in range(1,num+1):
    if num%i==0:
        li.append(i)
x=len(li)
if x==2:
    print("the number is a prime number")
else:
    print("not a prime number")
