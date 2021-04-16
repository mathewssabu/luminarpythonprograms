num=int(input("enter number to be reversed"))
s=0
while(num>0):
    s=s*10+num%10
    num=num//10

print(s)