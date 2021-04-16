num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter number 3"))
if((num1>num2)&(num1>num3)):
    print(" greatest", num1)
elif((num2>num1)&(num2>num3)):
    print("greatest",num2)
elif((num1==num2)&(num2==num3)):
    print("all are equal")
else:
    print("greatest",num3)