# Functions

'''
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.


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


'''

#Return a result from function

def my_function():
  return "Python is programming language"

output = my_function()

print(output)


#Function Arguments

'''
The following are the types of arguments that we can use to call a function:
Pass by Reference vs. Value
Default arguments
Keyword arguments
Required arguments
Variable-length arguments
The Anonymous Functions or Lamda functions
'''

#Pass by Reference vs. Value
'''
we modify the value of an argument within a function, the change is also reflected in the calling function.
'''

# defining the function  
def square( my_list ):  
    '''''This function will find the square of items in list'''  
    squares = []  
    for l in my_list:  
        squares.append( l**2 )  
    return squares  
  
# calling the defined function  

list_ = [45, 52, 13];  
result = square( list_ )  
print( "Squares of the list is: ", result )  