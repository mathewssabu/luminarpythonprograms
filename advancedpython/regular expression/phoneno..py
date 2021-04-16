import re
# num=input("enter a no.")
# x="\d{10}"
# match=re.fullmatch(x,num)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

num=input("enter a no.")
x="[+][9][1]\d{10}"
match=re.fullmatch(x,num)
if match is not None:
    print("valid")
else:
    print("not valid")


