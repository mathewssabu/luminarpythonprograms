class Student:
    def __init__(self,rno,name,course,total):
        self.rno=rno
        self.name=name
        self.course=course
        self.total=total

    def __str__(self):
        return self.name

ob1=Student(1,"mathews","python",100)
ob2=Student(2,"krish","python",100)
ob3=Student(3,"sub","python",100)
studs=[]
studs.append(ob1)
studs.append(ob2)
studs.append(ob3)
tot=list(map(lambda st:st.total,studs))
print(tot)
cour=list(filter(lambda num:num.course=="python",studs ))
for i in cour:
   print(i)