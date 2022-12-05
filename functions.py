# Functions

'''
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
'''


#Creating a Function

def my_function():
  print("Python is " + "awesome")

  
#Calling a Function

my_function()


#Arguments

#Information can be passed into functions as arguments.

def my_function(x,y):
  print("x=" + str(x)  + ",y=" + str(y))

my_function(1,2)
my_function(3,4)
my_function(5,6)




#Return a result from function

def my_function():
  return "Python is programming language"

output = my_function()

print(output)


#Pass by Reference vs. Value
'''
we modify the value of an argument within a function, the change is also reflected in the calling function.
'''

# defining the function  
def square( my_list ):
    print('square function calling')
    '''''This function will find the square of items in list'''  
    squares = []  
    for i in my_list: 
        print(i)
        squares.append( i**2 )  
    return squares  
  
# calling the defined function  

my_list = [5, 10]
print( "before ", my_list )
result = square( my_list )  
print( "after: ", result )


#Lamda functions

'''
it's a small anonymous function.

It can take any number of arguments, but can only have one expression.

syntax:

lambda arguments : expression

usage:

We can use them as an anonymous function inside another function.

same function definition to make a function that always doubles and triples the number

'''

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) # output: 22
print(mytripler(11)) # output: 33



#Function Arguments
'''
The following are the types of arguments that we can use to call a function:
Required arguments
Default arguments
Keyword arguments
Variable-length arguments
'''

#Required arguments
def print_me( str ):
   print(str)
   return str
   
print_me() # output: TypeError: print_me() takes exactly 1 argument (0 given)


#Keyword arguments
def print_info(name,age):
   print("Name:",name)
   print("Age:",age)
   return(name,age)

print_info(name="nagamani", age=25)

print_info(name="nagamani", age=25)

#Default arguments
def print_info(name="deena"):
   print("Name:",name)
   return name

print_info()
print_info("nagamani")


#variable length arguments

'''

*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)

* means wildcard

'''

# *args(Non-Keyword Arguments)
#example
def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Hello', 'Welcome', 'to', 'python tutorial')
#output
'''
Hello
Welcome
to
python tutorial
'''

#**kwargs (Keyword Arguments)
#example
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
myFun(first='Hello', mid='Welcome to', last='python tutorial')

#output
'''
first == Hello
mid == Welcome to
last == python tutorial
'''