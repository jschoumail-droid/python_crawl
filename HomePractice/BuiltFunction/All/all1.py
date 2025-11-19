'''
all 參數接收一個迭代器，如果迭代器所有元素的值為True,
那麼all函數的值才為True。
注意若參數本身為空列表all的值則為True

The all() function returns True if all items in an iterable are true, 
otherwise it returns False.
If the iterable object is empty, the all() function also returns True.

Syntax
all(iterable)

Parameter Values

Parameter	     Description
 iterable	An iterable object (list, tuple, dictionary)
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
x = all(mydict)