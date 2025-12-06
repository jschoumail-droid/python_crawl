'''
filter 函數用於過濾元素,它的使用形式如下:
  filter(function, sequnce)
將 function 依次作用於 sequnce 的每個項目，
  將返回值為 True 的項目組成一個 「迭代器」 返回。
  例如一個我們想要取得一個列表的所有偶數:
  我們先定義一個函數isEven,
  用來判斷一個正整數是否為偶數
'''
print('=====ex1=====')
def isEven(x):
    return x % 2 == 0
even_num = list(filter(isEven, [1, 2, 3, 4, 5, 6]))
print(even_num)

nums = [1, 2, 3, 4, 5, 6]
even_num = [x for x in nums if x % 2 == 0]
print(even_num)

even_num = list(filter(lambda x: x%2==0, [1, 2, 3, 4, 5, 6]))
print(even_num)

# 語法與map一樣，filter(欲執行的function名稱, 可迭代物件的名稱)
# 同map，filter回傳一個生成器物件，可以將它轉換成list

print('=====ex2=====')

names=['Karen','Jim','Kim']
lst1=list(filter(lambda name:len(name)==3,names))

nums=list(range(1000))
filtered=filter(lambda x:x%3==0 or x%7==0,nums)
sumOfFilter=sum(filtered)

print(lst1)
print(sumOfFilter)

print('=====ex3=====')
'''
filter()函式可以幫我們篩選可疊代的物件(Iterable Object)元素
'''
numbers = [50, 2, 12, 30, 27, 4]
result = list(filter(lambda x: x > 10, numbers))
print(result)  #執行結果：[50, 12, 30, 27]

result1 = [number for number in numbers if number > 10]
print(result1)  # 執行結果：[50, 12, 30, 27]