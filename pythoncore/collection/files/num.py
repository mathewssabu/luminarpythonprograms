h=open("numbers","r")
lst=[]
for lines in h:
    lst.append(lines)
sum=0
for i in lst:
    j=int(i)                #rstrip  remove nth character rstrip("\n")
    sum=sum+j               #lstrip remove first character

print(sum)