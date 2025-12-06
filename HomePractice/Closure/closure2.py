print('=====ex1=====')
def apply_async(fun,args,*,callback):
    #計算結果
    result=fun(*args)
    #以算出的結果來調用回乎函式
    callback(result)

def add(x,y):
    return x+y

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