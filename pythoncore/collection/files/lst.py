f=open("numbers","r")
lste=[]
lsto=[]
for num in f:
    i=int(num)
    if(i%2==0):
        lste.append(i)
    else:
        lsto.append(i)

print(sum(lste),sum(lsto))