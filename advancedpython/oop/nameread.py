class Name:
    def getdata(self,name,age,branch,mark):
        self.name=name
        self.age=age
        self.branch=branch
        self.mark=int(mark)

    def print(self):
        #if(self.mark>=190):
           print("name=",self.name,":   age= ",self.age,"branch=",self.branch,"mark=",self.mark)

f=open("names","r")
o=Name()
for lines in f:
   word=lines.split(",")
   #o=Name()
   o.getdata(word[0],word[1],word[2],word[3])
   if(int(word[3])>190):
     o.print()
   #print(word)

