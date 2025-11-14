
#ex1
class Pet():
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

#此處__init__()繼承父類別
class Cat(Pet):
    isFeline=True

class Dog(Pet):
    isFeline=False

myCat=Cat('Kibbles',8)
print('Cat name:',myCat.name)
print('Cat weight:',myCat.weight)

#ex2
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

jess=Baby('Jessie','Mcdonald')
tom=Adult('Thomas','Smith')

jess.speak()
tom.speak()