import re
num=input("enter a no.")
x="^a[a-zA-Z0-9\W]*b$"
match=re.fullmatch(x,num)
if match is not None:
    print("valid")
else:
    print("not valid")