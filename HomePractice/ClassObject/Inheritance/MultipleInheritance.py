#ex1
print("==ex1==")
class Animal():
    def __init__(self,name):
        self.name=name #private attribute，可由arg設定
    def fly(self): #public method
        print(self.name+"很會飛")

class Bird(Animal):
    def __init__(self,name):
        self.name="粉紅色"+name #覆蓋富類別屬性，private attribute，可由arg設定
    def sing(self): #public method
        print(self.name+"也會唱歌")

pigeon=Animal("小白鴿")
#pigeon.name="??" #correct
pigeon.fly() #public method

parrot=Bird("小鸚鵡")
#parrot.name="xxx" #correct
parrot.fly() #inheried method
parrot.sing() 

import datetime

#ex2
print("==ex2==")
class Person():
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

class Baby(Person):
    def speak(self):
        print('Blah blah blah')

class Adult(Person):
    def speak(self):
        print('Hello, my name is %s' % (self.firstName))

class Calendar():
    def bookAppointment(self,date):
        print('Booking appointment for date %s' % (date))

class OrganizeAdult(Adult,Calendar):
    pass

class OrganizeBaby(Baby,Calendar):
    def bookAppointment(self,date):
        print('Note that you are booking an appointment with a baby.')
        super().bookAppointment(date)

andres=OrganizeAdult('Andres','Gomez')
boris=OrganizeBaby('Boris','Bumblebutton')
andres.speak()
boris.speak()
boris.bookAppointment(datetime.date(2025,1,1))

#ex3 同名方法解析順序:由左至右讀取繼承列表的方法
print("==ex3==")
class Dog():
    def makeSound(self):
        print("Wolf!")

class Cat():
    def makeSound(self):
        print("Miaw!")

class DogCat(Dog,Cat):
    pass

myPet=DogCat()
myPet.makeSound()

#ex4
print("==ex4==")
class DogCat1(Cat,Dog):
    def makeSound(self):
        for i in range(3):
            super().makeSound()
            
myPet=DogCat1()
myPet.makeSound()

#ex5 練習
print("==ex5==")
class Polygon():
    """
    class:Polygon
    """
    def __init__(self,sideLengths):
        self.sideLengths=sideLengths

    def __str__(self):
        return "Polygon has %s sides" % self.numSides

    @property
    def numSides(self):
        return len(self.sideLengths)
    @property
    def perimeter(self):
        return sum(self.sideLengths)
    
class Rectangle(Polygon):
    """
    class:Rectangle
    """
    def __init__(self,height,width):
        super().__init__([height,width,height,width])
    @property
    def area(self):
        return self.sideLengths[0]*self.sideLengths[1]
    
class Square(Rectangle):
    def __init__(self,width):
        super().__init__(width,width)

print(Polygon.__doc__)
print(Rectangle.__doc__)
print(Square)

r=Rectangle(1,5)
t1=r.numSides,r.area
print(t1)
print(r.__str__())

s=Square(5)
t2=s.numSides,s.area
print(t2)
print(s.__str__())