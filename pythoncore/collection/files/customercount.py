f=open("customer","r")
dic={}
for i in f:
    words=i.rstrip("\n").split(",")
    for num in words:
       if(num not in dic):
          dic[num]=1
       else:
          dic[num]+=1
for j in dic:
    print(j,":",dic[j])