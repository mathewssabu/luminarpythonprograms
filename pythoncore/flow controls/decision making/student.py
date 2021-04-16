totcls=int(input("enter total clses"))
atcls=int(input("enter attended clses"))
atnd=(atcls/totcls)*100
if(atnd>=75):
    print("u r allowed")
else:
    print("u r not allowed")