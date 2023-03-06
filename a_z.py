import string as s
string_alpha="abcdefghijklmnopqrstuvwxyz"
st=string_alpha.upper()
print(st)
list_alpha=list(string_alpha)

for i in list_alpha:
    print(i,end=" ")
print("\n")
for i in string_alpha:
    print(i,end=" ")
print("\n")
for i in st:
    print(i,end=" ")
print("\n")
for i in s.ascii_lowercase:
    print(i,end=" ")
