'''
The isinstance() function returns True if the specified object is of 
the specified type, otherwise False.
If the type parameter is a tuple, this function will return True 
if the object is one of the types in the tuple.

Syntax
isinstance(object, type)

Parameter Values
Parameter	Description
object	    Required. An object.
type	    A type or a class, or a tuple of types and/or classes
'''
#ex1
print('=====ex1=====')
'''
Check if the number 5 is an integer
'''
print(isinstance(5, int))

#ex2
print('=====ex2=====')
'''
Check if "Hello" is one of the types described in the type parameter
'''
x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(x)

#ex3
print('=====ex3=====')
'''
Check if y is an instance of myObj
'''
class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)
print(x)