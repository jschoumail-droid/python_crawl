'''
Python Iterator 的定義為：符合 Python 中的 Iterator Protocol,
或是一個有 __iter__() 和 __next__() methods 的 object。

Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
'''
#ex1
print('=====ex1=====')
'''
Return an iterator from a tuple, and print each value:
'''
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#ex2
print('=====ex2=====')
'''
Strings are also iterable objects, containing a sequence of characters
'''
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#ex3
print('=====ex3=====')

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter),end=' ')
print(next(myiter),end=' ')
print(next(myiter),end=' ')
print(next(myiter),end=' ')
print(next(myiter),end=' ')
print()

#ex4
print('=====ex4=====')
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x, end=' ')
print()