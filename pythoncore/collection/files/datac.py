f=open("data","r")
dic={}
for num in f:
    words=num.rstrip("\n").split(" ")
print(words)
for i in words:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1

for j in dic:
    print(j,":",dic[j])