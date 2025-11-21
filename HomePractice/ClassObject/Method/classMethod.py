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

print('=====ex1=====')
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

print('=====ex2=====')
class Australian():
    isHuman=True
    enjoysSport=True

    @classmethod
    def isSportyHuman(cls):
        return cls.isHuman and cls.enjoysSport
    
print('Is Austrilian sporty human? ',Australian.isSportyHuman())

print('=====ex3=====')
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

print('=====ex4=====')

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
