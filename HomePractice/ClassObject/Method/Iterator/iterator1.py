'''
可以透過兩種主要方法製作迭代器：
使用類別(class)並實作 __iter__ 和 __next__ 方法：這是一種標準的物件導向方法，
  可以在類別中定義 __iter__ 方法來返回迭代器本身，並在 __next__ 方法中實作產生
  下一個值的邏輯。當沒有更多值可生成時,__next__ 應拋出 StopIteration 異常。
使用生成器函式(generator function):這是製作迭代器更簡潔的方式,只需在普通函式
中使用 yield 關鍵字即可。每次 yield 被執行時，它會暫停函式的執行並回傳一個值。
當函式下次被呼叫時，它會從上次暫停的地方繼續執行。 
'''
'''
方法二：使用生成器函式
這是製作迭代器最常見且簡潔的方式。

一個Node類別表示樹狀結構
實作一個迭代器,已先行深入的模式巡訪各節點
'''
print('=====ex1=====')
class Node:
    def __init__(self,value):
        self._value=value
        self._children=[]
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def addChild(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depthFirst(self):
        #print(f'self:{self}')
        yield self
        for c in self:
            #print(f'in:{c}')
            yield from c.depthFirst()
            
root=Node(0)
child1=Node(1)
child2=Node(2)
root.addChild(child1)
root.addChild(child2)
child1.addChild(Node(3))
child1.addChild(Node(4))
child2.addChild(Node(5))

'''
nd=iter(root)
print(next(nd))
print(next(nd))
nd=iter(child1)
print(next(nd))
print(next(nd))
nd=iter(child2)
print(next(nd))
'''

for ch in root.depthFirst():
    #pass
    print(ch,end=' ')
print()

'''
方法一：使用類別實作
這種方法適合需要更複雜狀態管理的情況。

一個Node類別表示樹狀結構
實作一個迭代器,已先行深入的模式巡訪各節點
python的迭代器協定要求__iter__()回傳一個特殊的迭代器物件,這個物件得實作一個
__Next__()方法,並使用StopIteration例外來標示迭代完成。然而這種物件的實作通
常很麻煩。如下例子:
'''
print('=====ex2=====')
class Node:
    def __init__(self,value):
        self._value=value
        self._children=[]
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def addChild(self,otherNode):
        self._children.append(otherNode)
    def __iter__(self):
        return iter(self._children)
    def depthFirst(self):
        return DepthFirstIterator(self)
    
class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''
    def __init__(self,startNode):
        self._node=startNode
        self._childrenIter=None
        self._childIter=None
    def __iter__(self):
        return self
    def __next__(self):
        #如果剛啟動,就回傳自己;為子節點建立一個迭代器
        if self._childrenIter is None:
            self._childrenIter=iter(self._node)
            return self._node
        
        #如果正在處理一個子節點,就回傳它的下一個項目
        elif self._childIter:
            try:
                nextchild=next(self._childIter)
                return nextchild
            except StopIteration:
                self._childIter=None
                return next(self)
        #前進到下一個節點並啟動它的迭代動作
        else:
            self._childIter=next(self._childrenIter).depthFirst()
            return next(self)

root=Node(0)
child1=Node(1)
child2=Node(2)
root.addChild(child1)
root.addChild(child2)
child1.addChild(Node(3))
child1.addChild(Node(4))
child2.addChild(Node(5))

for ch in root.depthFirst():
    print(ch, end=' ')
print()
    
'''
方法一：使用類別實作
這種方法適合需要更複雜狀態管理的情況。
'''
print('=====ex3=====')
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self  # 迭代器本身就是它的迭代器

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration # 沒有更多值時拋出異常

# 使用範例
my_iterator = MyIterator(5)
for num in my_iterator:
    print(num,end=' ') # 輸出：0, 1, 2, 3, 4
print()
 
'''
方法二：使用生成器函式
這是製作迭代器最常見且簡潔的方式。
'''
print('=====ex4=====')
def my_generator(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

# 使用範例
my_gen = my_generator(5)
for num in my_gen:
    print(num,end=' ') # 輸出：0, 1, 2, 3, 4
print()

# 也可以直接使用 next() 逐步呼叫
my_gen_next = my_generator(3)
print(next(my_gen_next),end=' ') # 輸出：0
print(next(my_gen_next),end=' ') # 輸出：1
print(next(my_gen_next),end=' ') # 輸出：2
# print(next(my_gen_next)) # 再次呼叫會拋出 StopIteration
print()