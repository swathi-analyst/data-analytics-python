salary=int(input("Enter Your Salary:"))
age=int(input("Enter Your Age:"))

if(salary>=20000 or age<=20):
    loan_amount=int(input("Enter the required loan amount:"))
    if(loan_amount>50000):
        print("Maximum loan amount is 50000")
    else:
        print("You are eligible for Loan.")
else:
    print("You are Not Eligible for Loan.")

#Hackrank Question Nested-If
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
