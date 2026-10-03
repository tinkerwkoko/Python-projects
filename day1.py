import math
import sys
print(sys.version)

#Open the python interactive shell and do the following operations. The operands are 3 and 4
#addition
x = 3
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x % y)
print(x / y)
print(x ** y)
print(x // y)

fname = "Kosi"
lname = "Amamchukwu"
country = "Nigeria"

print(f"My name is {fname} {lname}. I am from {country}. I am enjoying 30 days of Python.")

#Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Asabeneh", "Python", "Finland"]))
print(type(fname))
print(type(lname))
print(type(country))


#Find an Euclidean distance between (2, 3) and (10, 8):
x1 = 2
y1 = 3
x2 = 10
y2 = 8

r = (x1 - y1)
s = (x2 - y2)
d = math.sqrt(r ** 2 + s ** 2)

print(d)