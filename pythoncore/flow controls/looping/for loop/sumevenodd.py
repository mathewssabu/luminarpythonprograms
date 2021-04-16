low=int(input("enter lower"))
up=int(input("enter upper"))
sume=sumo=0
for i in range(low,up+1):
    if(i%2==0):
        sume+=i
    else:
        sumo+=i


print("sum of even=",sume)
print("sum of odd=",sumo)