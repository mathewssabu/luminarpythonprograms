lst=[4,2,1,6,7,8]
lst1=[]
for i in lst:
    if(i<5):
        lst1.append(i-1)
    else:
        lst1.append(i+1)

print(lst1)
result=list(map(lambda num: num-1 if num<5  else num+1,lst))
print(result)