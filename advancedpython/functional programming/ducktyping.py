class Shift:
    def start(self):
        print("start in shift")
    def accelerate(self):
        print("accelerate in shift")

class Innova:
    def start(self):
        print("start in innova")
    def accelerate(self):
        print("accelerate in innova")

class Person:
    def drive(self,ob):
        ob.start()
        ob.accelerate()

sf=Shift()
ino=Innova()
p=Person()
p.drive(sf)