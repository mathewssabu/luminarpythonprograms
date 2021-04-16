import re
# r="helloo3"
# x="\w{6}"
# match=re.fullmatch(x,r)
# if match is not None:
#    print("valid")
# else:
#    print("invalid")

r="56kg"
x="\d{2}[kg]"
match=re.fullmatch(x,r)
if match is not None:
    print("valid")
else:
    print("invalid")
