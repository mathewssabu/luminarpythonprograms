age=int(input("enter age"))
s=input("enter sex M or F ")
m=input("marital status Y or N")
if(s =='F'):
    print("urban areas")
else:
    if((age>=20)&(age<=40)):
        print("work anywhere")
    elif((age>40)&(age<=60)):
        print("urban areas only")
    else:
        print("error")