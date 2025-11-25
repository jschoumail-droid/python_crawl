'''
yield from是Python 中用於將一個生成器的操作委託給另一個生成器的語法。
  它的主要用法是簡化生成器的嵌套,允許一個生成器直接從子生成器或
  任何可迭代物件中「產出」(yield)所有值，而無需明確使用內層循環。
  這使得程式碼更簡潔、可讀性更高。 
用法詳解
簡化程式碼:yield from iterable相當於for item in iterable: yield item,但更簡潔。
  嵌套生成器: 當yield from後面接的是一個生成器時,它將子生成器的所有值直接傳給
  委派生成器的呼叫者。
傳遞資料:yield from不僅是簡單的迭代,它還允許子生成器直接接收從委派生成器外部發送的
  值(send())以及直接傳遞異常(throw())。委派生成器會在子產生器恢復執行後繼續運作。
  傳回值的取得: 當子產生器執行完畢並傳回一個值時,yield from表達式會捕獲這個值並將其
  傳回委派產生器。 
'''
print('=====ex1=====')
def np_range(n):
    for i in range(0 - n, 0):
        yield i

    for i in range(1, n + 1):
        yield i

# 顯示[-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
print(list(np_range(5)))
'''
Python 3.3 新增了 yield from 語法，上面的程式片段可以直接改寫為以下實作：
'''
def np_range(n):
    yield from range(0 - n, 0)
    yield from range(1, n + 1)

# 顯示[-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
print(list(np_range(5)))

'''
假設要統計一個超市所有分店的庫存,分店內部可能還有更小的分店。
使用yield from可以簡化嵌套結構:
此範例中,yield from count_inventory(branch)可以避免寫成嵌套的
for迴圈來處理分店裡的分店。 
'''
print('=====ex2=====')
def count_inventory(branches):
    for branch in branches:
        if isinstance(branch, list):
            yield from count_inventory(branch) # 委托给子分支
        else:
            yield branch # 产出库存物品

# 示例用法
store_inventory = [
    "item1",
    ["item2", "item3"],
    "item6",
    ["item5", ["item4"]]
]

for item in count_inventory(store_inventory):
    print(item, end=' ')