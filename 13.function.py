#Example[Function]
def painter():
    print("Paint My villa.")
painter()


def painter(worker):
    print("Paint My villa.",worker)
worker=input("Enter a Worker Name:")
painter(worker)


#Eercise-1 [Finding add() sub() mul() div()]
def add():
    print("ADDITION")
    a=int(input("Enter a num1:"))
    b=int(input("Enter a num2:"))
    print("Add=",a+b) 

def sub():
    print("SUBTRACTION")
    c=int(input("Enter a num3:"))
    d=int(input("Enter a num4:"))
    print("Sub=",c-d)

def mul():
    print("MULTIPLICATION")
    e=int(input("Enter a num5:"))
    f=int(input("Enter a num6:"))
    print("Mul=",e*f)

def div():
    print("DIVISION")
    g=int(input("Enter a num7:"))
    h=int(input("Enter a num8:"))
    print("Div=",g/h)

add()
sub()
mul()
div()


#Eercise-2 [Example]
def painter(Msg):
    print("Message:",Msg)

painter("Festival is near so please,Paint My Home Quickly.")


#Eercise-3 [Finding even or odd]
def evenorodd(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")
number=int(input("Enter a number:"))
evenorodd(number)


#Eercise-4 [Finding pass or fail]
def findpassorfail(Mark):
    if(Mark>35):
        print("Pass")
    else:
        print("Fail")
mark=int(input("Enter your Mark:"))
findpassorfail(mark)


#Eercise-5 [Finding a range]
def printrange(a,b):
    for i in range(a,b):
        print(i)
a=int(input("Enter a:"))
b=int(input("Enter b:"))
printrange(a,b)

