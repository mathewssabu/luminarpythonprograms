class Stud:
    def __init__(self,name,rno,dept,mark):
        self.name=name
        self.rno=rno
        self.dept=dept
        self.mark=mark
    def print(self):
        print(self.name,self.rno,self.dept,self.mark)

f=open("6","r")
max=0
for lines in f:
    word=lines.rstrip("\n").split(",")
    name=word[0]
    rno=word[1]
    dept=word[2]
    mark=int(word[3])
    o=Stud(name,rno,dept,mark)
    if (mark==200):
        o.print()


