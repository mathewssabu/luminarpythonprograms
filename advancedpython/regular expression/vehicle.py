import re
x="[a-zA-Z]{2}\d{2}[a-zA-Z]{2}\d{4}$"
f=open("vechicle no","r")
for lines in f:
    lines=lines.rstrip("\n")
    match = re.fullmatch(x,lines)
    if match is not None:
        print("valid")
    else:
        print("invalid")
