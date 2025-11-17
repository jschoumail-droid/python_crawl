'''
Python 裝飾詞 (Decorator) 被大量廣泛的使用在各方 library,是非常實用和必須了解的基礎
'''
#ex1
print('=====ex1=====')
'''
在 def timer(func): 將 func 變數名稱傳入，接下來定義 def wrap(sleep_time) 函式，
並且在裡面將剛剛傳入的 func(sleep_time) 調用，這樣就完成一個簡單的裝飾詞
'''
import time

def timer(func):
    def wrap(sleep_time):
        t_start = time.time()
        func(sleep_time)
        t_end = time.time()
        t_count = t_end - t_start
        print('[花費時間]', t_count)
    return wrap

def dosomething(sleep_time):
    print('do some thing')
    time.sleep(sleep_time)

foo = timer(dosomething)
foo(3)

#ex2
print('=====ex2=====')
'''
如果不想寫成 foo = timer(dosomething)，只需要加上 @timer,並直接調用 dosomething() 函式執行
'''

def timer(func):
    def wrap(sleep_time):
        t_start = time.time()
        func(sleep_time)
        t_end = time.time()
        t_count = t_end - t_start
        print('[花費時間]', t_count)
    return wrap

@timer
def dosomething(sleep_time):
    print('do some thing')
    time.sleep(sleep_time)

dosomething(3)
#裝飾詞在被 wrap 包一層後，其 __name__ 屬性就會被修改成 wrap
print(dosomething.__name__)

#ex3
print('=====ex3=====')
'''
如果要消除這個副作用的話，可以使用 python 內建的 functools,
只需要在 def wrap()之前，加上 @wraps(func)，即可獲得原先的 __name__ 屬性 dosomething
'''
from functools import wraps

def timer(func):
    @wraps(func)
    def wrap():
        t_start = time.time()
        func()
        t_end = time.time()
        t_count = t_end - t_start
        print('[花費時間]', t_count)
    return wrap

@timer
def dosomething():
    print('do some thing')

dosomething()
print(dosomething.__name__)

#ex4
print('=====ex4=====')
'''
如果有兩個 Decorator 裝飾詞要使用的話怎麼辦，其實只需要加在上面一行即可，順序的話會從上而下觸發
'''
from functools import wraps

def timer(func):
    @wraps(func)
    def wrap():
        t_start = time.time()
        func()
        t_end = time.time()
        t_count = t_end - t_start
        print('[花費時間]', t_count)
    return wrap

def func_print_one(func):
    @wraps(func)
    def wrap():
        print('this is func_print_one')
        func()
    return wrap

def func_print_two(func):
    @wraps(func)
    def wrap():
        print('this is func_print_two')
        func()
    return wrap

@timer
@func_print_one
@func_print_two
def dosomething():
    print('do some thing')

dosomething()

#ex5
print('=====ex5=====')
'''
在 def wrap() 和 func() 中加入 *args, **kargs 即可調用參數
'''
from functools import wraps

def timer(param: str):
    def timer_func(func):
        @wraps(func)
        def wrap(*args, **kargs):
            t_start = time.time()
            print(param)
            value = func(*args, **kargs)
            t_count = time.time() - t_start
            print(f"Function '{func.__name__}' spend: {t_count} s")
            return value
        return wrap
    return timer_func

@timer("Print before function start")
def dosomething(a, b):
    print(f"Count: {a + b}")

dosomething(1, 2)

#ex6
print('=====ex6=====')
'''
Class 的方法來寫裝飾詞的話，會將 wrap 寫在 __call__ 裡面來調用
'''
from functools import wraps

class Timer:
    def __init__(self, time_sleep):
        print('[__init__]')
        print('[time_sleep]:', time_sleep)
        self.time_sleep = time_sleep

    def __call__(self, func):
        @wraps(func)
        def wrap(*args, **kargs):
            t_start = time.time()
            time.sleep(self.time_sleep)
            value = func(*args, **kargs)
            t_end = time.time()
            t_count = t_end - t_start
            print('[共花費時間]', t_count)
            return value
        return wrap

@Timer(time_sleep=3)
def dosomethingClass(a, b):
    print('do some thing')
    print('a + b = ', a + b)

dosomethingClass(1, 2)