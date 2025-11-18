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
取出姓名字首為T,並將其轉換為大寫
'''
names=['Graham Chapman','John Cleese','Terry Gilliam',
       'Eric Idle','Terry Jones']
print([name.upper() for name in names if name.startswith('T')])

#ex2
print('=====ex2=====')
'''
使用多個輸入list
'''
print([x*y for x in ['spam','eggs','chips'] for y in [1,2,3]])
print([x*y for x in [1,2,3] for y in ['spam','eggs','chips']])

numbers=[1,2,3]
print([x**y for x in numbers for y in numbers])

#ex2
print('=====ex2=====')
'''
錦標賽比賽分組(1對1)
'''
names=['Graham Chapman','John Cleese','Terry Gilliam',
       'Eric Idle','Terry Jones']
fixtures=[f"{p1} vs. {p2}" for p1 in names for p2 in names if p1!=p2]
for i in fixtures:
    print(i)