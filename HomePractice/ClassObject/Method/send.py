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

print('=====ex3=====')
def coroutine_example():
    print("協程啟動")
    while True:
        received = yield
        print(f"接收到的數據: {received}")

# 啟動生成器協程
gen = coroutine_example()
next(gen)  # 啟動協程
gen.send("第一個數據")
gen.send("第二個數據")

print('=====ex4=====')
def event_driven_generator():
    print('開始接收外部事件')
    event_count = 0
    while True:
        event = yield event_count
        if event == "click":
            event_count += 1
        elif event == "reset":
            event_count = 0
        print(f"事件數量: {event_count}")

gen = event_driven_generator()
next(gen)  # 啟動生成器

# 模擬事件
gen.send("click")
print(gen.send("click"))
gen.send("reset")
gen.send("click")

print('=====ex5=====')
def data_stream_processor(data):
    print(f'接收資料')
    total = 0
    for item in data:
        total += item
        print(f'處理第{item}個資訊 :{total}')
        processed_value = yield total
        if processed_value is not None:
            total = processed_value
            print(f'處理接收的資訊 :{total}')

gen = data_stream_processor([1, 2, 3, 4, 5])
print(next(gen))  # 處理第一個數據
print(gen.send(10))  # 更新總和為 10 並繼續
print(next(gen))  # 繼續處理
print(next(gen))  # 繼續處理
print(gen.send(10))  # 更新總和為 10 並繼續
