'''
The zip() function returns a zip object, which is an iterator of 
  tuples where the first item in each passed iterator is paired together,
  and then the second item in each passed iterator are paired together etc.
If the passed iterables have different lengths, the iterable with the least 
  items decides the length of the new iterator.

Syntax
  zip(iterator1, iterator2, iterator3 ...)
Parameter Values
  Parameter	Description
  iterable1, iterable2, iterable3 ...
'''
print('=====ex1=====')
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(list(x))

'''
If one tuple contains more items, these items are ignored:
'''
print('=====ex2=====')
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(list(x))
