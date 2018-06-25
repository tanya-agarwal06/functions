'''class Complex():
    def __init__(self,real,imag):
        self.r=real
        self.i=imag
c=Complex(2,3)
print(c.i)
print(c.r)'''

class Apollo():
    destination = "Moon"
    def __init__(self):
        print("ready to launch")
    def flying(self):
         print("spaceship is flying")
    def getdestination(self):
            print("the destination is" + self.destination)
c=Apollo()
c.flying()
c.getdestination()
b=Apollo()
b.destination=" mars "
b.getdestination()




