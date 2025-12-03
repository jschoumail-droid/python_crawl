print('=====ex1=====')
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

print('=====ex2=====')
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

print('=====ex3=====')
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

print('=====ex4=====')
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