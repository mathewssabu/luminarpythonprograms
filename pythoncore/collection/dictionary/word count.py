line="hai hello hai hello hai"
word=line.split(" ")
dic={}
for i in word:
    if((i in dic)==False):
        dic[i]=1
    else:
        dic[i]+=1


for i in dic:
    print(i,dic[i])