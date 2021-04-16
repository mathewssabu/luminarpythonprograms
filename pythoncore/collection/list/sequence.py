lst=[3,4,8]
lst1=[]
sum=0
for i in lst:
    sum+=i

for i in range(0,3):
    a=sum-lst[i]
    lst1.append(a)

print(lst1)

