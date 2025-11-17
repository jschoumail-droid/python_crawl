#ex1
print('=====ex1=====')
'''
計算執行迴圈所需時間
'''
import random
import time

start=time.time()
#start=time.time_ns()
l=[random.randint(1,999) for _ in range(100*3)]
#print(l)
end=time.time()
#end=time.time_ns()
print(end-start)