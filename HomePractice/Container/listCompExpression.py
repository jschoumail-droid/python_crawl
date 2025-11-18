'''
串列(List)Comprehension的語法包含三個部分,說明如下:
[expression for item in iterable]
expression:可以是 item 或運算式。
item:接收可疊代的物件(Iterable Object)元素。
iterable:可疊代的物件(Iterable Object)。
'''
#ex1
print('=====ex1=====')
'''
三種組成1~5立方值得串列
'''
cubes=[]
for x in [1,2,3,4,5]:
    cubes.append(x**3)
print(cubes)

cubes1=[x**3 for x in [1,2,3,4,5]]
print(cubes1)

cubes2=[x**3 for x in range(1,6)]
print(cubes2)

#ex2
print('=====ex2=====')
'''
在串列(List)Comprehension中利用條件判斷來篩選元素時,則可以使用下列語法
[expression for item in iterable (if condition)]
'''
#取出姓名字首為T,並將其轉換為大寫
names=['Graham Chapman','John Cleese','Terry Gilliam',
       'Eric Idle','Terry Jones']
print([name.upper() for name in names if name.startswith('T')])
#取出0~9內大於4的數值乘3後組成串列
numbers = [x * 3 for x in range(10) if x > 4]
print(numbers)

#ex3
print('=====ex3=====')
'''
使用多個輸入list
'''
print([x*y for x in ['spam','eggs','chips'] for y in [1,2,3]])
print([x*y for x in [1,2,3] for y in ['spam','eggs','chips']])

numbers=[1,2,3]
print([x**y for x in numbers for y in numbers])

#ex4
print('=====ex4=====')
'''
錦標賽比賽分組(1對1)
'''
names=['Graham Chapman','John Cleese','Terry Gilliam',
       'Eric Idle','Terry Jones']
fixtures=[f"{p1} vs. {p2}" for p1 in names for p2 in names if p1!=p2]
for i in fixtures:
    print(i)

#ex5
print('=====ex5=====')
'''
map()函式可以將特定運算式套用至可疊代的物件(Iterable Object)元素
'''
numbers = [50, 2, 12, 30, 27, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  #執行結果：[100, 4, 24, 60, 54, 8]

result1 = [number * 2 for number in numbers]
print(result1)  #執行結果：[100, 4, 24, 60, 54, 8]

#ex6
print('=====ex6=====')
'''
filter()函式可以幫我們篩選可疊代的物件(Iterable Object)元素
'''
numbers = [50, 2, 12, 30, 27, 4]
result = list(filter(lambda x: x > 10, numbers))
print(result)  #執行結果：[50, 12, 30, 27]

result1 = [number for number in numbers if number > 10]
print(result1)  # 執行結果：[50, 12, 30, 27]