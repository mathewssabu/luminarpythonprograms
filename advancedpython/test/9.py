import re
num=input("enter a no.")
x="^[A-Z]{1}[a-z]+"
match=re.fullmatch(x,num)
if match is not None:
    print("valid")
else:
    print("not valid")