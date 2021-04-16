import re
m=input("enter mail id")
x="([a-z][a-z0-9_+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)"
match=re.fullmatch(x,m)
if match is not None:
    print("valid")
else:
    print("invalid")