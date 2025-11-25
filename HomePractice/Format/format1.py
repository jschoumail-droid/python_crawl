'''
Python 中 r 的用法主要有兩種：在字串前加 r 作為 「原始字串」，
  用於取消轉義符（例如在處理檔案路徑時），
以及在 str.format() 函式中使用 !r,表示使用 repr()
  函數來格式化字串。 
r 作為原始字串前綴
  作用：在字串前加上 r,可以防止反斜線 \ 被解釋為轉義字符。
  應用：這對於處理包含大量反斜線的字串特別有用，例如 Windows 檔案路徑。
範例：
  print(r"C:\new\nfile") 會印出 C:\new\nfile。
  print("C:\new\nfile") 會印出 C:\new 加上一個換行，然後是 file。 
!r 作為 str.format() 的格式化指令
  作用：在 str.format() 中，!r 是一個格式化指令，它會對傳入的物件呼叫 repr() 函數，而不是 str() 函數。
  應用：這會將物件轉換成 Python 解釋器可以理解的表示形式，通常會在字串前後加上引號。
範例：
print("{!r}".format("hello")) 會印出 'hello'。
print("{}".format("hello")) 會印出 hello。 
總結
  符號 	 說明
  r	    在字串前加上 r,表示此字串為「原始字串」,取消轉義字符的處理。
  !r	在 str.format() 中，表示使用 repr() 函數來格式化字串。
'''
print('=====ex1=====')
print("{!r}".format("hello")) #會印出 'hello'。
print("{}".format("hello")) #會印出 hello。

'''
位置參數：在 {} 中填入數字來指定參數的順序。
'''
print('=====ex2=====')
print('{} is {} years old.'.format('John', 20))
# 輸出：John is 20 years old.
print('{1} is {0} years old.'.format('John', 20))
# 輸出：20 is John years old.

'''
關鍵字參數：使用變數名稱作為佔位符
'''
print('=====ex3=====')
print('{name} is {age} years old.'.format(name='John', age=20))
# 輸出：John is 20 years old.

'''
無序插入:format() 方法可以接受任意數量的參數，位置可以不按順序
轉義大括號：使用雙大括號 {{}} 來顯示字面上的大括號
'''
print('=====ex4=====')
print('{} is {{}}'.format('hello'))
# 輸出：hello is {}

'''
dict 插入:format() 方法
'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
       'Dcab: {0[Dcab]:d}'.format(table))
#Jack: 4098; Sjoerd: 4127; Dcab: 8637678

'''
也可以用'**' 符號,把table 當作傳遞的關鍵字參數。
'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

'''
進階用法（格式規格）
  對齊：使用 ^、<、> 來分別表示居中、左對齊、右對齊。
    print('{:<10}'.format('hello')) # 左對齊,寬度10
  寬度：在對齊符號後加上數字來指定最小寬度。
    print('{:>10}'.format('hello')) # 右對齊,寬度10
  精度:f 格式用於浮點數，.2f 表示保留兩位小數。
    print('{:.2f}'.format(1.123)) # 輸出:1.12
  填充：在對齊符號前指定填充字符。
    print('{:^10}'.format('hello')) # 中間對齊,寬度10
  數字格式：
    +號    會在正數前顯示 +，負數前顯示 -。
    (空格) 會在正數前加一個空格。
    % 號   會將數字轉換為百分比形式。
    , 號   會在數字中加入千位分隔符。 
'''
print('=====ex5=====')
name = "小明"
age = 25
print("姓名：{}，年齡：{}".format(name, age))
# 輸出：姓名：小明，年齡：25
price = 1234.567
print("價格是：{:,}".format(price))
# 輸出：價格是：1,234.567
print("價格是：{:,.2f}".format(price))
# 輸出：價格是：1,234.57

'''
格式化字串(簡稱為f-字串)在字串前加上前綴f或F,透過{expression}表達式
,把Python 表達式的值加到字串內。
'''
print('=====ex6====')
import math
print(f'pi={math.pi:.3f}.')
'''
在':'後傳遞整數，為此欄位設定最小字元寬度，常用於列對齊：
'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

'''
還有一些修飾符可以在格式化前轉換值。
'!a'應用ascii(),'!s'應用str(),'!r'應用repr():
'''
print('=====ex7====')
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
#My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
#My hovercraft is full of 'eels'.

'''
手動格式化方式實現的同一個平方和立方的表
'''
print('=====ex8====')
for x in range(1, 4):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

'''
str.zfill()，該方法在數字字串左邊填充零，且能辨識正負號
'''
print('=====ex9====')
print('12'.zfill(5))
#00012
print('-3.14'.zfill(7))
#-003.14
print('3.14159265359'.zfill(5))
#3.14159265359

'''
舊式字串格式化方法
'''
print('=====ex10====')
import math
print('pi=%5.3f.' % math.pi)