'''
callback
use function
'''
print('=====ex1=====')
def apply_async(fun,args,*,callback):
    #計算結果
    result=fun(*args)
    #以算出的結果來調用回乎函式
    callback(result)
    
def print_result(result):
    print('Got:',result)
    
def add(x,y):
    return x+y

apply_async(add,(2,3),callback=print_result)
apply_async(add,('Hello','World'),callback=print_result)

'''
use class method
'''
print('=====ex2=====')
class ResultHandler:
    def __init__(self):
        self.sequence=0
    def handler(self,result):
        self.sequence+=1
        print(f'[{self.sequence}] Got: {result}')

r=ResultHandler()
apply_async(add,(4,5),callback=r.handler)
apply_async(add,('Hello','World'),callback=r.handler)

'''
use closure
'''
print('=====ex3=====')
def make_handler():
    sequence=0
    def handler(result):
        nonlocal sequence
        sequence+=1
        print(f'[{sequence}] Got: {result}')
    return handler
        
handler=make_handler()
apply_async(add,(8,5),callback=handler)
apply_async(add,('Hello','World'),callback=handler)

'''
use coroutine(協程)
'''
print('=====ex4=====')
def make_handler1():
    sequence=0
    while True:
        result = yield
        sequence+=1
        print(f'[{sequence}] Got: {result}')

handler1=make_handler1()
next(handler1) #前進到yield
apply_async(add,(7,5),callback=handler1.send)
apply_async(add,('Hello','World'),callback=handler1.send)

print('=====ex5=====')
class SequenceNo:
    def __init__(self):
        self.sequence=0
        
def handler(result,seq):
    seq.sequence+=1
    print(f'[{seq.sequence}] Got: {result}')
    
seq=SequenceNo()
from functools import partial

apply_async(add,(7,8),callback=partial(handler,seq=seq))
apply_async(add,('Hello','World'),callback=partial(handler,seq=seq))