n=int(input("enter the range: "))


for i in range(1,n+1):
    li=[]
    for j in range(1,n+1):
        if i%j==0:
            li.append(i)
    x=len(li)
    if x==2:
        print(i,end=" ")

