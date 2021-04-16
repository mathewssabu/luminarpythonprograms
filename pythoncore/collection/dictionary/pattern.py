pattern="abcdbca"
#word=pattern.split("")
l=len(pattern)
dic={}
for i in pattern:
    if(i not in dic):
        dic[i]=1
    else:
        print(i)
        break