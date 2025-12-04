'''
map 函數形式 : map(function, sequence)
對 sequence 中的 item 依次執行 function(item),
並將結果組成一個 「迭代器」 返回。
也就是：(function(item1), function(item2), function(item3), ...)。
例如一個數字列表有正有負，
我們想要把裡面每個數字取絕對值，
'''
print('=====ex1=====')

nums= [1,-2,-3]
ans = map(abs,nums)
print(list(ans))

nums= [1,-2,-3]
ans = [abs(x) for x in nums]
print(ans)

ans=list(map(lambda x:abs(x),nums))
print(ans)

# map(欲執行的function名稱, 可迭代物件的名稱)
# map回傳一個生成器物件，可以將它轉換成list

print('=====ex2=====')

names=['Magda','Jose','Anne']

#method 1
lengths=[]
for name in names:
    lengths.append(len(name))

print(lengths)
print('average length=',sum(lengths)/len(lengths))

#method 2
lengths1=[]
lengths1=list(map(len,names))

print(lengths1)
print('average length=',sum(lengths1)/len(lengths1))

print('=====ex3=====')
'''
map()函式可以將特定運算式套用至可疊代的物件(Iterable Object)元素
'''
numbers = [50, 2, 12, 30, 27, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  #執行結果：[100, 4, 24, 60, 54, 8]

result1 = [number * 2 for number in numbers]
print(result1)  #執行結果：[100, 4, 24, 60, 54, 8]

            