#Data types
'''
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Boolean Type:	bool
None Type:	NoneType
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
'''

#1. Text Type:	str

x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 


#2.Numeric Types: int, float, complex

#Python Numbers:
'''
There are three numeric types in Python:
int
float
complex
'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


#3.Boolean Type: bool

x = True

#display x:
print(x)

#display the data type of x:
print(type(x))


#4. None Type: NoneType

x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 


#4.1 additional example

emp_name = None
print("before joined " + str(emp_name))

is_emp_joined = True #flag either it may true or false

if is_emp_joined:
    emp_name = "nagamani"
else:
    emp_name = ""
print("after joined " + emp_name)