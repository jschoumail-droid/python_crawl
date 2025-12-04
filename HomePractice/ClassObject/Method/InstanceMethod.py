'''
Python 的 class 本身不能被直接呼叫執行，但有幾種方式可以「呼叫」它或類別中的方法。
  你需要先建立一個物件實例，然後才能呼叫該物件實例的方法。或者，你可以使用
  @staticmethod 裝飾器，這樣該類別中的方法就可以像靜態方法一樣直接從類別名稱呼叫，
  而不需要實例。
  另一種方式是透過實作 __call__ 方法，讓這個 class 實例本身變成可以被呼叫的物件。 
建立物件後呼叫
  這是最常見的方式，你需要先建立 class 的物件，然後呼叫物件的方法
'''
print('=====ex1.1=====')
class MyClass:
    def my_method(self):
        print("這是 my_method")

my_object = MyClass() # 建立物件實例
my_object.my_method() # 呼叫物件的方法

'''
使用 @staticmethod 裝飾器可以將一個方法定義為靜態方法，這樣就可以直接從 class 呼叫，
  而不需要建立物件
'''
print('=====ex1.2=====')
class MyClass:
    @staticmethod
    def my_static_method():
        print("這是靜態方法")

MyClass.my_static_method() # 直接從 class 呼叫

'''
實現 __call__ 方法
如果一個類別實作了 __call__ 方法，那麼該類別的物件實例就可以像函數一樣被呼叫。 
'''
print('=====ex1.3=====')
class MyCallableClass:
    def __call__(self):
        print("物件實例被呼叫了")

my_callable_object = MyCallableClass()
my_callable_object() # 直接呼叫物件實例


print('=====ex2=====')
import math
print()
#__init__()就是instance method
class Circle():
    isShape=True
    def __init__(self,radius,color='red'):
        self.radius=radius
        self.color=color
    def area(self):
        return math.pi*self.radius**2
    
circle=Circle(3)
print(circle.area())
print(circle.color)

print('=====ex3=====')
class Pet():
    def __init__(self,height,name):
        self.height=height
        self.name=name
    
    isHuman=False
    owner="Michael Smith"

    def isTall(self,tallIfAtLeast):
        return self.height>=tallIfAtLeast
    def __str__(self):
        return '%s (height: %s cm)' % (self.name,self.height)

onePet=Pet(40,'chubbles')
print(onePet) #以__str__方法顯示，若無此方法，python 顯示 <__main__.Pet object at ......>
print(onePet.height)
print("is tall? ",onePet.isTall(30))

print('=====ex4=====')
class Country():
    def __init__(self,name="unspecified",population=None,sizeKmsq=None):
        self.name=name
        self.population=population
        self.sizeKmsq=sizeKmsq
    def sizeMilesSq(self,conversionRate=0.621371):
        return self.sizeKmsq*conversionRate**2
    def __str__(self):
        label=self.name
        if self.population:
            label='%s, population: %s' % (label,self.population)
        if self.sizeKmsq:
            label='%s, size kmsq: %s' % (label,self.sizeKmsq)
        return label
    
'''algeria=Country(name='Algeria',population=100)
print(algeria) #以__str__方法顯示，若無此方法，python 顯示<__main__.Country object at 0x0000007E3EA63B80>'''
algeria=Country(name='Algeria',sizeKmsq=2.382e6,population=100)
print(algeria) #以__str__方法顯示，若無此方法，python 顯示<__main__.Country object at 0x0000007E3EA63B80>
print("Country area of {} is {}".format(algeria.name,algeria.sizeMilesSq(conversionRate=0.6)))
#查看物件的特性清單
print("dict: ",algeria.__dict__)

print('=====ex5=====')
def apply_async(fun,args,*,callback):
    #計算結果
    result=fun(*args)
    #以算出的結果來調用回乎函式
    callback(result)

def add(x,y):
    return x+y

class ResultHandler:
    def __init__(self):
        self.sequence=0
    def handler(self,result):
        self.sequence+=1
        print(f'[{self.sequence}] Got: {result}')

r=ResultHandler()
apply_async(add,(4,5),callback=r.handler)
apply_async(add,('Hello','World'),callback=r.handler)