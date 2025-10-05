import sys

a =20
print(a)

a = "Heloo"
print(a)

# id(a)  memory address check krne ke liye

print(id(a))

print(sys.getsizeof(a))

x = 10
y = 20

print(x)
print(y)

x = 12
x = "Hello World"
print(x)
print(x)

# assign multiple values

x,y,z = 10,22,33

print(x,y,z)

# One Value to Multiple Variables

# x = y = z = "Oral"

# print(x)
# print(y)
# print(z)

# Unpack A Collection
"""fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
