'''
reduce 函數形式 : reduce (function, sequnce)
首先將 sequence 的前兩個 item 傳給 function,
即 function(item1, item2),
函數的返回值和 sequence 的下一個 item 再傳給 function,
即 function(function(item1, item2), item3),
如此迭代，直到 sequence 沒有元素。
例如: reduce(f, [x1, x2, x3, x4]) 代表的值為
f(f(f(x1, x2), x3), x4)。
reduce適合用在需要重複化簡列表內元素的情況
'''
print('=====ex1=====')
from functools import reduce
def prod(x,y):
    return x*y
print(reduce(prod, [4,5,6]))

#from functools import reduce
print(reduce(lambda x, y : x*y, [4,5,6]))

print('=====ex2=====')
from functools import reduce
class final_grade:
    bonus=3
    def __init__(self,name='name',gra='grade',HW=0,mid=0,final=0):
        self.name=name
        self.grade=gra
        self.hw=HW
        self.mid=mid
        self.fin=final
    def weight(self):
        hw_w=0.25
        mid_w=0.35
        fin_w=0.4
        return [hw_w,mid_w,fin_w]
    def rank(self):
        score=[self.hw,self.mid,self.fin]
        we=self.weight()
        print(we)
        print(score)
        #lst=list(map(lambda x,y:x*y,score,we))
        #print(lst)
        #print(reduce(lambda a,b:a+b,lst))
        return reduce(lambda a,b:a+b,map(lambda x,y:x*y,score,we))
A=final_grade('Jack','4',80,70,85)
print(A.rank())
#output:78.5
print(A.__dict__)
#output:{'name': 'Jack', 'grade': '4', 'hw': 80, 'mid': 70, 'fin': 85}
print(final_grade.__dict__)
#output:
#{'__module__': '__main__', 
#'bonus': 3
#'__init__': <function final_grade.__init__ at memory>, 
#'weight': <function final_grade.weight at memory>,..., 
#'__dict__': <attribute '__dict__' of 'final_grade' objects>, 
#'__weakref__': <attribute '__weakref__' of 'final_grade' objects>, 
#'__doc__': None}