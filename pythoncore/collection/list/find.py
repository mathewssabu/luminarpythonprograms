lst=[23,24,35,56,27]             #LINEAR SEARCH
a=int(input("enter element to be found"))
flag=0
for i in lst:
    if(i==a):
        flag=1
        break

if(flag==1):
       print("element found")
else:
       print("element not found")