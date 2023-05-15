
dic={"name":"1","age":"19","university":"3"}
print(dic["university"])
d1={1:"leo madarchod",2:"ram"}
print(d1,type(d1))
print(dic)
# dic.update(d1)
print(dic.update({"leo madarchod":"hlo"}))
print(dic)
print(len(dic))
d1.clear()
print(d1)
# del dic["age"]
print(dic)
# print(dic.pop("names","invalid"))


# dic.pop("namee")
print(dic)
print(type(dic.items()))
print(dic.keys())

d=sorted(dic.values())
print(d)
sorted(dic)
print(dic)
dic.popitem
print(dic.popitem())
dicc=[1,2,3,4,5,6,8]
a=dict.fromkeys(dicc,"100")
print(a)