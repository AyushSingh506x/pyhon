st=input("enter the string: ")
res={key:st.count(key) for key in st.split()}
print(res)