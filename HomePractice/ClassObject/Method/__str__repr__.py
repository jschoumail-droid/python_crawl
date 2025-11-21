print('=====ex1=====')
'''
當我們print一個物件時,若該物件未定義特定的顯示方法,Python 
會輸出該物件的記憶體位置資訊。例如：
'''
class Cat:
    pass

kitty = Cat()
print(kitty) #<__main__.Cat object at 0x0000006006F1E7D0>


print('=====ex2=====')
'''
__str__
用於定義物件的「可讀字串表示」，通常是給使用者看的。
當使用 print() 函數或 str(obj) 時,會呼叫此方法

__repr__
用於定義物件的「正式字串表示」，通常是給開發者看的，應該提供物件的詳細資訊。
當在直譯器中直接輸入物件名稱時，或使用 repr(obj) 時，會呼叫此方法。

如果物件同時定義了 __str__ 和 __repr__,則 print(obj) 會優先使用 __str__。
如果物件只定義了 __repr__,則 print(obj) 和 repr(obj) 都會使用 __repr__。
'''
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"str = {self.name}"

    def __repr__(self):
        return f"repr = {self.name}"

kitty = Cat('安安')
print(kitty) #str = 安安

print('=====ex3=====')
'''
如果無__str__ 方法，只保留 __repr__
'''
class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"repr = {self.name}"

kitty = Cat('安安')
print(kitty) #repr = 安安