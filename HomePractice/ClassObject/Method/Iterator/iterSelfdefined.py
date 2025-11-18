#ex1
print('=====ex1=====')
'''
找出小於100的質數組成之串列
'''
class PrimesBelow():
    def __init__(self,bound):
        self.candidateNumbers=list(range(2,bound))

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.candidateNumbers)==0:
            raise StopIteration
        nextPrime=self.candidateNumbers[0]
        self.candidateNumbers=[x for x in self.candidateNumbers if x % nextPrime !=0]
        return nextPrime
    
primesToHundred=[prime for prime in PrimesBelow(100)]
print(primesToHundred)

#ex2
print('=====ex2=====')
'''
Create an iterator that returns numbers, starting with 1, 
and each sequence will increase by one (returning 1,2,3,4,5 etc.):
'''
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

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#ex3
print('=====ex3=====')
'''
To prevent the iteration from going on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error 
if the iteration is done a specified number of times:

Stop after 20 iterations:
'''
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
  print(x)