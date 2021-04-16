def calculator():
    i=int(input("enter a choice (1-4)"))
    a=int(input("enter 1st num"))
    b=int(input("enter 2nd num"))
    if(i==1):
        print("sum=",a+b)
    elif(i==2):
        print ("diff=",a-b)
    elif(i==3):
        print("product=",a*b)
    elif(i==4):
        print("quotient=",a/b)
    else:
        print("wrong option")
calculator()