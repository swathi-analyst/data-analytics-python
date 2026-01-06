#Exercise-1
s_username="EMC"
s_password=123

def validate(username,password):
    if(username==s_username and password==s_password):
        return "True"
    else:
        return "False"
name=input("Enter a u_name=")
passcode=int(input("Enter a u_passcode="))
a=validate(name,passcode)
print(a)

#Exercise-2
def add(a,b):
    return (a+b)*c
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
value=add(a,b)
print(value)

#Exercise-2 [Easy  way]
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

def add(n1,n2):
    return n1+n2

sum=add(a,b)
output=sum*c
print(output)
