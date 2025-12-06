'''
Python類別(Class)中有@classmethod裝飾詞(Decorator)的方法(Method),
  被呼叫時，相較於實體方法(Instance Method)的self參數指向物件(Object),
  類別方法(Class Method)為cls參數,指向類別(Class)

由於類別方法(Class Method)的cls參數指向類別(Class)，所以類別方法(Class Method)
  僅能改變類別的狀態，而無法改變物件(Object)的狀態,因為它沒有self參數可以存取
  物件的屬性(Attribute)及方法(Method)。如下範例
'''
print('=====ex1.1=====')
# 汽車類別
class Cars:
    door = 4  # 類別屬性
    # 類別方法(Class Method)
    @classmethod
    def open_door(cls):
        print(f"{cls} has {cls.door} doors.")
mazda = Cars()
mazda.open_door()  #透過物件呼叫
Cars.open_door()  #透過類別呼叫

'''
另外,Python的類別方法(Class Method)常應用於產生物件(Object)，如下範例
'''
print('=====ex1.2=====')
# 汽車類別
class Cars:
    # 建構式
    def __init__(self, seat, color):
        self.seat = seat
        self.color = color
    # 廂型車
    @classmethod
    def van(cls):
        return cls(6, "black")
    # 跑車
    @classmethod
    def sports_car(cls):
        return cls(4, "yellow")
van = Cars.van()
sports_car = Cars.sports_car()

'''
Use cases: Class methods are often used for:
Alternative constructors: Providing different ways to
  create instances of the class, often by processing input
  in a specific format.
Factory methods: Creating and returning instances of 
  the class or other related classes based on certain conditions.
Modifying class state: Changing class variables that affect 
  all instances of the class.
Example:
'''

print('=====ex2=====')
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def change_class_variable(cls, new_value):
        cls.class_variable = new_value
        print(f"Class variable changed to: {cls.class_variable}")

    @classmethod
    def create_from_string(cls, data_string):
        # An alternative constructor
        instance_var = data_string.upper()
        return cls(instance_var)

c1=MyClass(10)
#c1.class_variable='changed by c1'
# Accessing the class variable directly
print(MyClass.class_variable)
print('c1=',c1.class_variable,c1.instance_variable)

# Calling a class method on the class
MyClass.change_class_variable("New Value")
print('after change class var, c1=',c1.class_variable,c1.instance_variable)
c2=MyClass(20)
print('new obj, c2=',c2.class_variable,c2.instance_variable)

# Creating an instance using a class method (alternative constructor)
obj = MyClass.create_from_string("hello world")
print(obj.instance_variable)
print(obj.class_variable) # Instances also reflect the updated class 

#類別方法類似於實例方法，不同之處在於
#  實例方法的第一個位置引數self傳遞的是物件實例，類別方法的第一個位置引數是類別本身。
#  與靜態方法一樣，可以使用修飾器(@classmethod)宣告類別方法。

print('=====ex3=====')
class Australian():
    isHuman=True
    enjoysSport=True

    @classmethod
    def isSportyHuman(cls):
        return cls.isHuman and cls.enjoysSport
    
print('Is Austrilian sporty human? ',Australian.isSportyHuman())

print('=====ex4=====')
#用類別方法擴展Coubtry類別
class Country():
    def __init__(self,name="unspecified",population=None,sizeKmsq=None):
        self.name=name
        self.population=population
        self.sizeKmsq=sizeKmsq
    
    @classmethod
    def creatWithMsq(cls,name,population,sizeMsq):
        sizeKmsq=sizeMsq/0.621371**2
        return cls(name,population,sizeKmsq)
    
mexico=Country.creatWithMsq('Mexico',150e6,760000)
print(mexico.sizeKmsq)

print('=====ex5=====')

import random

#用類別方法擴展Pet類別
class Pet():
    def __init__(self,height):
        self.height=height
    
    isHuman=False
    owner="Michael Smith"

    @classmethod
    def ownedBySmithFamily(cls):
        return 'Smith' in cls.owner

    @classmethod
    def createRandomHeightPet(cls):
        height=random.randrange(1,100)
        return cls(height)

onePet=Pet(40)
onePet.owner='john'
otherPet=Pet(60)
print(onePet.owner,Pet.owner)
print(otherPet.owner,Pet.owner)
print('height=',onePet.height)
print('Does owned by smith damily?',Pet.ownedBySmithFamily())

for i in range(5):
    pet=Pet.createRandomHeightPet()
    print('Pet height :',pet.height)


print('=====ex6=====')
class MyClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def create_with_default(cls):
        # Accesses class_variable
        return cls(cls.class_variable * 2) 

    @classmethod
    def get_class_variable(cls):
        return cls.class_variable