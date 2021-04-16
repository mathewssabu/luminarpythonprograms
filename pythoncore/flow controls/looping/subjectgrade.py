sub1=int(input("enter sub 1 marks out of 50"))
sub2=int(input("enter sub 2 mark"))
sub3=int(input("enter sub 3"))
sub4=int(input("enter sub 4"))
total=sub1+sub2+sub3+sub4
p=total/2
if(p>=90):
    print("A+")
elif((p>=80)&(p<=89)):
    print("A")
elif((p>=70)&(p<=79)):
    print("B+")
elif((p>=60)&(p<=69)):
    print("B")
elif((p>=50)&(p<=59)):
    print("C+")
elif((p>=40)&(p<=49)):
    print("C")
elif((p>=30)&(p<=39)):
    print("D+")
else:
    print("fail")