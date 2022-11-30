#variable: it is a  containers for storing data values.
#Creating Variables
x = 10
y = "Nagamani"
print(x)
print(y)

#Get the Type: get the data type of a variable with the type().
print(type(x))
print(type(y))

#Casting: If we want to specify the data type of a variable
a = str(3)    # a will be '3'
b = int(3)    # b will be 3
c = float(3)  # c will be 3.0
print(f' a= {a}, b= {b}, c={c}')

#Case-Sensitive: Variable names are case-sensitive.
a = "Nagamani"
A = "Nagamani"
print(a)
print(A)

#Ruls for python variables names
'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number

A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

#Multi Words Variable Names
#Variable names with more than one word can be difficult to read.

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "Nagamani1"
print(myVariableName)

#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "Nagamani2"
print(MyVariableName)

#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "Nagamani3"
print(my_variable_name)

#Assign Multiple Values
#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Output Variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x + y)

'''
#Global Variables: 

Variables that are created outside of a function

Global variables can be used by everyone, both inside of functions and outside.

'''

x = "awesome"

def my_function():
  print("Python is " + x)

my_function()


x = "awesome"

def my_function():
  x = "fantastic"
  print("Python is " + x)

my_function()

print("Python is " + x)
