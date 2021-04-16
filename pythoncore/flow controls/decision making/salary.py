salary=float(input("enter salary"))
yr=float(input("enter year of service"))
if(yr>5):
    bonus=salary*(5/100)
    print("bonus amnt=",bonus)
else:
    print("no bonus")