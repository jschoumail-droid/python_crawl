'''
顯然地,ex1的流程有別於函式中使用了 return,函式就結束了的情況。
實際上，當函式中使用 yield 產生值時，呼叫該函式會傳回 generator 物件，
也就是產生器，此物件具有 __next__ 方法，通常會使用 next 函式呼叫該方法
取出下個產生值（也就是 yield 的值），若無法產生下一個
(也就是含有yield的函式結束了),會發生StopIteration例外(Exception)
'''
print('=====ex1=====')
def xrange(n):
    x = 0
    while x != n:
        yield x
        x += 1

for n in xrange(10):
    print(n,end=' ') 
print()

print('=====ex2=====')
g = xrange(2)
print(type(g))
print(next(g))
print(next(g))
#print(next(g))

print('=====ex3=====')
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

print('=====ex4=====')
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

print('=====ex6=====')
def simple_generator():
    print('Step 1')
    yield 1
    print('Step 2')
    yield 2
    print('Step 3')
    yield 3

# 呼叫函式不會執行，而是回傳一個生成器物件
my_gen = simple_generator()
print(type(my_gen))

# 第一次呼叫 next()，執行到第一個 yield
print(next(my_gen))

# 第二次呼叫 next()，從上次暫停的地方繼續執行
print(next(my_gen))

# 也可以用 for 迴圈遍歷生成器
print('my_gen---')
for value in my_gen:
    print(value)
print('my_gen1---')
my_gen1 = simple_generator()
for value in my_gen1:
    print(value)

# 當生成器用盡時，會引發 StopIteration 錯誤
# print(next(my_gen))