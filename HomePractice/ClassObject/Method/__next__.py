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