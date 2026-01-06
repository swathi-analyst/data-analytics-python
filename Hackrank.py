#Question-1
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)

#Question-2
n=int(input())
if(n%2==0):
    if(n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("Weird")
    elif(n>20):
        print("Not Weird")
else:
    print("Weird")

#Question-3
a=int(input())
b=int(input())
print(a//b)
print(a/b)

#Question-4
n=int(input())
for i in range(n):
    print(i**2)
