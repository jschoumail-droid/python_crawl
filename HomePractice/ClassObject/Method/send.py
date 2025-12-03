print('=====ex1=====')
import random

def producer():
    while True:
        data = random.randint(0, 9)
        print('生產了：', data)
        yield data

def consumer():
    while True:
        data = yield
        print('消費了：', data)

def clerk(jobs, producer, consumer):
    print('執行 {} 次生產與消費'.format(jobs))
    p = producer()
    c = consumer()
    next(c)  
    for i in range(jobs):
        data = next(p)
        c.send(data)

clerk(3, producer, consumer) 


print('=====ex2=====')
def apply_async(fun,args,*,callback):
    #計算結果
    result=fun(*args)
    #以算出的結果來調用回乎函式
    callback(result)

def add(x,y):
    return x+y

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
