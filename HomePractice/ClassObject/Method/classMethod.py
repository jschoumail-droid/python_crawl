#類別方法類似於實例方法，不同之處在於
#  實例方法的第一個位置引數self傳遞的是物件實例，類別方法的第一個位置引數是類別本身。
#  與靜態方法一樣，可以使用修飾器(@classmethod)宣告類別方法。

class Australian():
    isHuman=True
    enjoysSport=True

    @classmethod
    def isSportyHuman(cls):
        return cls.isHuman and cls.enjoysSport
    
print('Is Austrilian sporty human? ',Australian.isSportyHuman())

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
print('height=',onePet.height)
print('Does owned by smith damily?',Pet.ownedBySmithFamily())

for i in range(5):
    pet=Pet.createRandomHeightPet()
    print('Pet height :',pet.height)
