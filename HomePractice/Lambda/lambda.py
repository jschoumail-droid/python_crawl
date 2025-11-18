#lambda 僅適用於1行的函式
# lambda arguments : expression

#ex1
print('=====ex1=====')
'''def addUp(x,y):
    return x+y'''

addUp = lambda x,y:x+y

print(addUp(2,5))

firstItem=lambda myList:myList[0]

print(firstItem(['cat','dog','mouse']))

#ex2
print('=====ex2=====')
'''
map()與lambda函式可以將特定運算式套用至可疊代的物件(Iterable Object)元素
'''
numbers = [50, 2, 12, 30, 27, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  #執行結果：[100, 4, 24, 60, 54, 8]

result1 = [number * 2 for number in numbers]
print(result1)  #執行結果：[100, 4, 24, 60, 54, 8]