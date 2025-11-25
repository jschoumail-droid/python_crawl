'''
如果不需要花俏的輸出,只想快速顯示變數進行調試,
  可以用repr()或str()函數把值轉換為字串。
str()函數傳回供人閱讀的值,repr()則產生適於解釋器讀取的值
(如果沒有等效的語法,則強制執行SyntaxError)。
對於沒有支援供人閱讀展示結果的對象,str()傳回與repr()相同的值。
一般情況下，數字、列表或字典等結構的值，使用這兩個函數輸出的
表現形式是一樣的。字串有兩種不同的表現形式。
'''
print('=====ex1=====')
s = 'Hello, world.'
print(str(s)) #Hello, world.
print(repr(s)) #'Hello, world.'
print(str(1/7)) #0.14285714285714285
x = 10 * 3.25
y = 200 * 200
s = 'x=' + repr(x) + ', y=' + repr(y) + '...'
print(s) #x=32.5, y=40000...
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos) #'hello, world\n'
# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs')))) #(32.5, 40000, ('spam', 'eggs'))