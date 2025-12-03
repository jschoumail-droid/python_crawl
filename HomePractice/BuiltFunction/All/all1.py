'''
Python 的 all() 函數會判斷一個可迭代物件（如列表或元組）中的所有元素是否都為 True。
  如果所有元素都為真，或者可迭代物件是空的，則返回 True:否則，只要有一個元素為 False
  ，就返回 False。0、None、False 和空字串在布林值轉換中都會被視為 False。 
用法
語法： all(iterable)
  iterable: 任何可迭代的物件，例如列表、元組、集合、字典或字串。 
範例
[True, True, True] 的 all() 結果為 True。
[True, False, True] 的 all() 結果為 False。
[1, 2, 0] 的 all() 結果為 False,因為 0 被視為 False。
[]（空列表）的 all() 結果為 True,因為它不包含任何 False 值。
["hello", "world"] 的 all() 結果為 True。
["hello", "", "world"] 的 all() 結果為 False,因為空字串 "" 被視為 False。 
'''

#ex1
print('=====ex1=====')

print(all(['a'<'b','b'<'c']))
print(all(['a'<'b',1<2, 0]))
print(all([]))

print('----------')

#Check if all items in a list are True:
mylist = [0, 1, 1]
print(all(mylist))

#Check if all items in a list are True:
mylist = [True, True, True]
print(all(mylist))

#Check if all items in a tuple are True
mytuple = (0, True, False)
print(all(mytuple))

#Check if all items in a set are True:
myset = {0, 1, 0}
print(all(myset))

#Check if all items in a dictionary are True:
mydict = {0 : "Apple", 1 : "Orange"}
mydict1 = {"Apple":20, "Orange":0}
x = all(mydict)
y = all(mydict1)
print(x,y)