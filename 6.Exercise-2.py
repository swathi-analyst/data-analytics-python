#Question 1
mark=int(input("Enter the mark:"))
if(mark>35):
    print("PASS")
else:
    print("FAIL")

#Question 2
income=int(input("Enter the income:"))
if(income>7000):
    print("Scholarship is Available.")
else:
    print("Scholarship is not Available.")

#Question 3
number=int(input("Enter the number:"))
if(number%3==0 and number%5==0):
    print(number," is divisible by both 3 and 5.")
else:
    print(number," is not divisible by both 3 and 5.")

#Question 4
num=int(input("Enter the number:"))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")

#Question 5
score=int(input("Enter the score:"))
if(score<35):
    print("Poor Student")
elif(score>35 and score<70):
    print("Average Student")
elif(score>70 and score<100):
    print("Good Student")
else:
    print("Invalid Value")

#Question 6
a=int(input("num1:"))
b=int(input("num2:"))
userinput=input("ADD/SUB/MUL/DIV:")
if(userinput=="ADD"):
    print("Addition=",a+b)
elif(userinput=="SUB"):
    print("Subtraction=",a-b)
elif(userinput=="MUL"):
    print("Multiplication=",a*b)
elif(userinput=="DIV"):
    print("Division=",a/b)
else:
    print("Invalid input")

#Question 7
score=int(input("Enter the score:"))
if(score>70):
    name=input("Name:")
    department=input("Department:")
    Location=input("Location:")
    print("You are eligible")
else:
    print("You are not eligible.")

#Question 8
sub1=int(input("Tamil="))
sub2=int(input("English="))
sub3=int(input("Maths="))
sub4=int(input("Science="))
sub5=int(input("Social="))
Total=(sub1+sub2+sub3+sub4+sub5)
avg_mark=Total/5
#print(Total," / ",avg_mark)
if(avg_mark<35):
    print("Additional Class is Required.")
else:
    print("You are Good to go.")
  