# Question-1
a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
for i in range(a+1,b):
    print(i)

# Question-2
for i in range(1,11):
    if(i%2==0):
        print(i)

# Question-3
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)

#Question-4
Odd=0
Even=0
for i in range(1,11):
    if(i%2==0):
        Even=Even+1
    else:
        Odd=Odd+1
print("Even:",Even)
print("Odd:",Odd)

#Question-5
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)

#Question-6
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)


#Question-7
a=[]
print("Enter a 10 Numbers")
for i in range(10):
    num=int(input("Enter num "+str(i+1)+"="))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print("Total:",sum)
print("Average:",sum/10)


n=int(input())
num=0
print("The first ",n,"Natural number is:")
for i in range(1,n+1):
    print(i,end=" ")
    num=num+i
print("\nSum =",num)

