

#1
radius=float(input("enter number"))
def area(rad):
    area= 3.14*rad*rad
    return area
ar= area(radius)
print(ar)

#2

def perfect(n):
    sum = 0
    for i in range(1,n):
         if(n%i==0):
             sum= sum + i
    if(sum==n):
        return True
    else:
        return False

for i in range(1,1001):
    if (perfect(i)== True):
        print("perfect number is:" +str(i))
    else:
        pass

#3
def mul_table(n, i=1):
    if i==11:
        return
    print(str(n) + " x " + str(i) + " = " + str(n*i))
    mul_table(n,i+1)

mul_table(int(input("enter number")))


#4
def power(x,y):
    if y==0:
        return 1
    else:
        return(x * power(x,y-1))
x=int(input("enter number"))
y=int(input("enter power"))
p = power(x,y)
print(p)

#5
A={}
def fact(n):
    if n==1:
        return 1
    else:
        f= n*fact(n-1)
        return(f)
x=int(input("enter number"))
ff=fact(x)
A[x]=ff
print("dictionary", A)
