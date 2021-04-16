import  re
f=open("7","r")
a=open("7final","a")
x="[+][9][1]\d{10}"
for line in f:
    line=line.rstrip("\n")
    match=re.fullmatch(x,line)
    if match is not None:
       a.write(line)
       a.write("\n")