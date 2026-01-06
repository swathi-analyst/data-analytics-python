#Exercise-1 [LIST]

# 1-append()
a=[1,2,3,4]
a.append(5)
a.append("True")
a.append("Apple")
print(a)

# 2-insert()
a=[1,2,3,4,5]
a[4]=6
a.insert(0,0)
print(a)

# 3-pop()
a=[1,2,3,4,5,6,7]
a.pop()   #Automaticlly removed ending value
a.pop(5)  #5th index position value 6 is removed by pop method.
print(a)

# 4-extend()
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b) # Merge two list into 1
print(a)


#Exercise-2 (TUPLE)
a=(1,2,3,4,5)
b=list(a)
b.append("ABCD")
b[5]=6
b.insert(4,"JKS")
print(type(b),"\n",b)
print(tuple(b),b)


#Exercise-3 {SET}
a={1,2,3,4,5}
a.add(6)
a.remove(4)
a.update("A")
a.pop()
print(a)


#Exercise-4 {DICTIONARY=Key:value}

a={
    "Name":"JK",
     "Age":25,
     "Degree":"Engineering",
     "Work":"Service Manager",
     "Work Field":["Bank","ATM"],
     "Location":["Dharmapuri","Krishnagiri","Hosur"]
   }

a.update({"Degree":"Mechanical Engineering"})

a["Bike"]="MT"

a.popitem()

a.pop("Location")


print(a)

print(a.keys())

print(a.values())

print(a.items())

