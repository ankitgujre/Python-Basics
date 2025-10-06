# following data type provided by python language
# * Buil in data types
# 1. None
# 2. Numeric
# 3. sequence
# 4. set
# 5. mapping
# 6. Boolean
# 7. Binary

# * User defined data types
#There are three numeric types in python
_int = 13
print(type(_int))

_float = 3.14
print(_float)

# Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# type conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Strings in python are surrounded by either single quotation marks, or double quotation marks.

g = "Helo"
g = 'Hello world'
print(g)

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

s = '"Hello "'
print(s)

s = "It's"
print(s)

# Multiline String

a = a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)