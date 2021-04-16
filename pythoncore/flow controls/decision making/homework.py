#birth month date yr
#today month date yr print age
bmonth=int(input("enter birth month"))
bdate=int(input("enter birth date"))
byr=int(input("enter birth yr"))
tmonth=int(input("enter today month"))
tdate=int(input("enter today date"))
tyr=int(input("enter today yr"))
if((tmonth>=bmonth)&(tdate>=bdate)):
    age=tyr-byr
elif(tmonth<bmonth):
    age=tyr-byr-1
elif(tmonth>bmonth):
     age=tyr-byr
elif(tmonth==bmonth):
    if(tdate>=bdate):
        age=tyr-byr
    else:
        age=tyr-byr-1


print(age)