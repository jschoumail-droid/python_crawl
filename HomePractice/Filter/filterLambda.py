# 語法與map一樣，filter(欲執行的function名稱, 可迭代物件的名稱)
# 同map，filter回傳一個生成器物件，可以將它轉換成list
#ex1
print('=====ex1=====')

names=['Karen','Jim','Kim']
lst1=list(filter(lambda name:len(name)==3,names))

nums=list(range(1000))
filtered=filter(lambda x:x%3==0 or x%7==0,nums)
sumOfFilter=sum(filtered)

print(lst1)
print(sumOfFilter)

#ex2
print('=====ex2=====')
'''
filter()函式可以幫我們篩選可疊代的物件(Iterable Object)元素
'''
numbers = [50, 2, 12, 30, 27, 4]
result = list(filter(lambda x: x > 10, numbers))
print(result)  #執行結果：[50, 12, 30, 27]

result1 = [number for number in numbers if number > 10]
print(result1)  # 執行結果：[50, 12, 30, 27]