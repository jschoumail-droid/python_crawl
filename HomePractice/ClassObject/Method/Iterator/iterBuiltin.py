'''
Python Iterator 的定義為：符合 Python 中的 Iterator Protocol,
或是一個有 __iter__() 和 __next__() methods 的 object。
'''
#ex1
print('=====ex1=====')

vowels = ['a', 'e', 'i', 'o', 'u']
print(hasattr(vowels, '__iter__')) #True
print(hasattr(vowels, '__next__')) #False

# 可以用 iter() 來宣告 iterator object
vowels_iter = iter(vowels)
print(hasattr(vowels_iter, '__iter__')) #True
print(hasattr(vowels_iter, '__next__')) #True

#ex2
print('=====ex2=====')
'''
可以用 collection module 來判斷是不是 iterator
'''
# Python 3.10+ 請用以下這行 import
from collections.abc import Iterable, Iterator
# Python 3.9- 請用以下這行 import
#from collections import Iterable, Iterator

vowels = ['a', 'e', 'i', 'o', 'u']
print(isinstance(vowels, Iterable)) #True
print(isinstance(vowels, Iterator)) #False

vowels_iter = iter(vowels)
print(isinstance(vowels_iter, Iterable)) #True
print(isinstance(vowels_iter, Iterator)) #True

#ex3
print('=====ex3=====')
'''
宣告了一個 list object 後,Python 會將這個 list object 存在記憶體當中，
也因此宣告完 list object後,你可以隨時取得這個 list object 的任意 item。
但這樣會有一個問題：當這個 list object 有很多 items 的時候，就會吃掉很多記憶體資源，
因此 iterator 就是用來解決這類問題的。
list object 的 iterator 版本就稱為 list iterator object。list iterator object和
普通的list object最大的不同就在於執行方式,不像list object會將所有items載入記憶體,
list iterator object宣告後就只能iterate所有item 一次，有點像是，我 iterate 完一個
item後,就把控制權丟出去,並且只需要記得目前這個iterator iterate到哪個 item 就好，
等到需要iterate的時候,再繼續iterate下一個item,有點類似linked list的概念
'''
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels[2])
# 可以隨時取得 list object 的任意元素'i'

vowels_iter = iter(vowels)
#print(vowels_iter[2]) #TypeError: 'list_iterator' object is not subscriptable
#只能用next來iterate iterator的items，且執行一次 next，
#就像是將 inked list的指標往後挪一個 item
print(next(vowels_iter)) #'a'
print(next(vowels_iter)) #'e'
print(next(vowels_iter)) #'i'
print(next(vowels_iter)) #'o'
print(next(vowels_iter)) #'u'
#iterate到最後一個item 後，再執行 iterator 的話，就會噴 StopIteration 的 exception
#print(next(vowels_iter)) #StopIteration

#記憶體用量比較
import sys
print(sys.getsizeof(vowels)) #104 (Bytes)
print(sys.getsizeof(vowels_iter)) #48 (Bytes)

#ex4
print('=====ex4=====')
'''
宣告 Iterator

iter function 語法
1. iter(object)
2. iter(object, sentinel)
如果沒有傳入第二個sentinel argument,那第一個object argument一定要是iterable object,
否則會raise TypeError
如果有傳入第二個 sentinel argument,那第一個 object argument 一定要是 callable object,
每次iterate都會call object argument的__next__() method,如果某個__next__()回傳的value
和sentinel argument一樣,那就會raise StopIteration,停止iterate
'''
list_instance = [1, 2, 3, 4]
print(iter(list_instance)) #<list_iterator object at 0x0000000D18D53CD0>
class DoubleIt:
    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start
    
    __call__ = __next__

my_iter = iter(DoubleIt(), 16)
print(my_iter) #<callable_iterator object at 0x0000000D18D53CA0>

for x in my_iter:
    print(x,end=' ') # 2 4 8
print()
'''
*** generator 也是一種 iterator,可以參考另一篇文章:Python Generator 介紹。
'''

#ex5
print('=====ex5=====')
class Interrogator():
    def __init__(self,questions):
        self.questions=questions

    def __iter__(self):
        return self.questions.__iter__()
    
questions=['Q1 ?','Q2 ?','Q3 ?','Q4 ?']
onePerson=Interrogator(questions)

for question in onePerson:
    print(question)