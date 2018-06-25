#1

class Animal():
    def animal_attribute(self):
        print("Animal attribute is called")
class Tiger(Animal):
    def show1(self):
        self.animal_attribute()
T=Tiger()
T.show1()

#2
print("a.f(),b,f() --AB")
print("a.f(),b,f() --AB")

#3
class Cop():
    def __init__(self):
        self.name=input("enter name ")
        self.age=int(input("enter age"))
        self.we=input("enter work experience")
        self.d=input("enter designation")
    def display(self):
        print("NAme=%s\tAge=%d\twork experience is=%s\tdesignation is=%s"%(self.name,self.age,self.we,self.d))
    def update(self):
        self.name=input("enter the updated name")
        self.age=int(input("enter updated age"))
        self.we=input("enter new work experience")
        self.d=input("enter updated designation")
class Mission(Cop):
    def add_mission_details(self):
        self.md=input("enter details %s ="%(self.name))

    def mission_display(self):
        print("name=%s\tage=%d\twrok experience=%s\tdesignation=%s\tMission=%s" % (self.name,self.age,self.d,self.we,self.md))
M=Mission()
M.display()
M.update()
M.display()
M.add_mission_details()
M.mission_display()

#4
class Shape():
    def show2(self):
        self.l = int(input("enter the length"))
        self.b = int(input("enter breadth"))
class rectangle(Shape):
    def area(self):
        self.show2()
        self.A = self.l*self.b
    def show1(self):
        print("area of rectangle is",self.A)
class Square(Shape):
    c=0
    def area(self):
        self.show2()
        if(self.l==self.b):
            self.A=self.l*self.l
            self.c=1
        else:
            print("enter same length and breadth")
    def show1(self):
        if(self.c==1):
            print("area of square", self.A)
        else:
             pass
R=rectangle()
S=Square()
R.show1()
S.area()
S.show2()