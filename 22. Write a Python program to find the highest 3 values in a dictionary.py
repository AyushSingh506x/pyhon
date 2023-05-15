di={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
li=di.values()
l2=sorted(li,reverse=True)
print(l2)
c=0
for i in l2:
    print(i)
    c+=1
    if c==3:
        break
