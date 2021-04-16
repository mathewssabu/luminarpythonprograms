def prime():
    num=int(input("enter number"))
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag+=1
            break

    if(flag==1):
        print("not prime")
    elif(flag==0):
        print("prime")
    s="thhhh"
    return s


t=prime()
print(t)
