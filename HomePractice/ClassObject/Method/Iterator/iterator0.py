'''
可以透過兩種主要方法製作迭代器：
使用類別(class)並實作 __iter__ 和 __next__ 方法：這是一種標準的物件導向方法，
  你可以在類別中定義 __iter__ 方法來返回迭代器本身，並在 __next__ 方法中實作產生
  下一個值的邏輯。當沒有更多值可生成時,__next__ 應拋出 StopIteration 異常。
使用生成器函式(generator function):這是製作迭代器更簡潔的方式，只需在普通函式中
  使用 yield 關鍵字即可。每次 yield 被執行時，它會暫停函式的執行並回傳一個值。
  當函式下次被呼叫時，它會從上次暫停的地方繼續執行。

方法一：使用類別實作
  這種方法適合需要更複雜狀態管理的情況
'''
print('=====ex1=====')
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
這是製作迭代器最常見且簡潔的方式
'''
print('=====ex2=====')
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
print(next(my_gen_next)) # 輸出：0
print(next(my_gen_next)) # 輸出：1
print(next(my_gen_next)) # 輸出：2
# print(next(my_gen_next)) # 再次呼叫會拋出 StopIteration