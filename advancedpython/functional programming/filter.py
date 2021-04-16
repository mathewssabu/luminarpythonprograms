#filter(function,iterables)
# lst=[12,232,424,111,33,1]
# even=list(filter(lambda num:num%2==0,lst))
# print(even)
lst=["asd","addf","wddd"]
aname=list(filter(lambda num:num[0]=='a',lst))
print(aname)