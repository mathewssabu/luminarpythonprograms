lst=[1,2,3,4,5,6]
a=int(input("enter number"))
l=len(lst)
for i in range(1,l+1):
    for j in range(1,l+1):
        if((i+j)==a):
            print("(",i," ",j,")")