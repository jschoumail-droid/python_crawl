'''
在〈for Comprehension〉可以使用 () 包括 for Compherension,
這會建立一個 generator 物件，這個物件也可以使用 for in 來迭代。
'''
print('=====ex1=====')
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
array = [element for row in matrix for element in row]
print(array)

print('=====ex2=====')
print([letter1 + letter2 for letter1 in 'Justin' for letter2 in 'momor'])

'''
舉個例子來說,Python 中有個 sum 函式，可以計算指定序列的數字加總值，
像是若傳遞 sum([1, 2, 3]) 的話，結果會是 6。如果想計算 1 到 10000 的加總值呢？
使用 sum([n for n in range(1, 10001)]) 是可以達到目的，不過，這會先產生具有
10000 個元素的 list,然後再交給 sum 函式運算，此時可以寫成
sum(n for n in range(1, 10001)) 就不會有產生 list 的負擔。
'''
print('=====ex3=====')
print(sum([n for n in range(1, 101)])) #此種寫法不佳，耗記憶體
print(sum(n for n in range(1, 101)))

print('=====ex4=====')
text = 'Your Right brain has nothing Left. \
Your Left brain has nothing Right'
print({c for c in text if c.isupper()})

print('=====ex5=====')
names = ['Justin', 'Monica', 'Irene']
passwds = [123456, 654321, 13579]
print({name : passwd for name, passwd in zip(names, passwds)})

'''
那麼，可以使用 for Comprehension建立 tuple嗎?可以的,不過不是在
  for Comprehension兩旁放上 ()，這樣的話就會建立一個 generator 物件，
  而不是 tuple,想要用 for Comprehension 建立 tuple 的話，可以將
  for Comprehension 產生器運算式傳給 tuple。例如:
'''
print('=====ex6=====')
print(tuple(n for n in range(10)))