low=int(input("enter lower"))
up=int(input("enter upper"))

for i in range(low,up+1):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
        else:
            flag=0
    if(flag==0):
        print(i)
