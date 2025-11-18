# map(欲執行的function名稱, 可迭代物件的名稱)
# map回傳一個生成器物件，可以將它轉換成list

#ex1
print('=====ex1=====')

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

#ex2
print('=====ex2=====')
'''
map()函式可以將特定運算式套用至可疊代的物件(Iterable Object)元素
'''
numbers = [50, 2, 12, 30, 27, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  #執行結果：[100, 4, 24, 60, 54, 8]

result1 = [number * 2 for number in numbers]
print(result1)  #執行結果：[100, 4, 24, 60, 54, 8]

            