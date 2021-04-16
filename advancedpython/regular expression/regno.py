import re
f=open("regno.","r")
f1=open("regnowrite","a")
x="[a-zA-Z]{3}[0-9]{2}[P][Y][0-9]{3}"
for lines in f:
    n=lines.rstrip("\n")
    match=re.fullmatch(x,n)
    if match is not None:
       f1.write(n)  
       f1.write("\n")

