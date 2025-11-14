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