'''
hasattr() 是 Python 中的一個內建函數，用於檢查一個對象是否具有指定的屬性或方法。
它接受兩個參數：要檢查的對象和一個表示屬性名稱的字串，
如果對象擁有該屬性，則回傳 True,否則回傳 False

語法
python
hasattr(object, name)
參數
object:要檢查的對象。
name:一個字串，表示要檢查的屬性或方法的名稱。 
回傳值
True:如果對象具有該屬性或方法。
False:如果對象不具有該屬性或方法。 
'''
class A:
    def __init__(self):
        self.name = "python"
    
    def func(self):
        return "This is a method"

obj = A()

print(hasattr(obj, 'name'))  # 輸出: True
print(hasattr(obj, 'age'))   # 輸出: False
print(hasattr(obj, 'func'))  # 輸出: True