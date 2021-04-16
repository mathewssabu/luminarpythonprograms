num=int(input("enter a number"))
s=0
for i in range(2,num):
     if(num%i==0):
         s+=1

if(s>=1):
    print("not prime number")

else:
    print(" prime number")
