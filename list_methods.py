leo= ["ayush","aka","leo"]
print(type(leo))#type function will tell the data type of the variable
leo.insert(3,"codm")#it will insert a item at a specific index
leo.insert(4,"ayush")
print(leo)
# leo.extend("ayush")
leo.remove("leo")#this function removes a specific item from the list
y=leo.count("ayush")#this function count how many times an item is repeated
print(y)
del leo[3]#this keyword or method del an item at an particular index
print(leo)

print(leo)
ayush=[1,3,4,2,0,6,1]
print(leo.index("ayush"))#this functions tell at which index is the item is present
for i in range(len(leo)):
    x=leo.pop()#pop( functon pop out the last item from the list )
    # if x is "[]":
        # break
    print(x)
leo.clear()#this function will clear the list
