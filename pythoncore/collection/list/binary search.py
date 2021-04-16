#algorithm

#1 sorting

#2 low=0
#   upp=(last element) len(lst)-1

#3 calculate mid
#mid=(low+upp)//2

#4 conditions
 #if(element>lst[mid])
 #low=mid+1
 #if(element<lst[mid])
 #upp=mid-1
 #if(element==lst[mid])
 #element found
lst=[9,1,3,4,2,5,6,8,7]
lst.sort()
low=0
up=len(lst)-1
flag=0
a=int(input("enter the value"))
while(low<=up):
    mid = (low + up) // 2
    if(a>lst[mid]):
        low=mid+1
    elif(a<lst[mid]):
        up=mid-1
    elif(a==lst[mid]):
         flag=1
         break

if(flag==1):
    print("found")
else:
    print("not found")