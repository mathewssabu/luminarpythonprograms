#100  60  100
 #60  100  40
#40    40  60
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("ebter num3"))
if((num1>num2)&(num1>num3)):
    if(num2>num3):
      print("secnd grtst",num2)
    else:
      print("scnd grtst",num3)
elif((num2 > num1) & (num2 > num3)):
      if(num1>num3):
        print("secnd grtst", num1)
      else:
          print("scnd grtst",num3)
elif((num3>num1)&(num3>num2)):
      if(num1>num2):
          print("scnd grtst",num1)
      else:
          print("scnd grtst",num2)
#elif()
else:
    print("secnd grtst",num3)
