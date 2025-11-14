class Australian():
    isHuman=True #public attribute
    enjoySport=True #public attribute

#john=Australian #不正確指定，但未顯示錯誤，下面statement除了type()有異外，其它皆無異樣。
john=Australian()
print(type(john))
print("iohn is human:",john.isHuman)
#john.enjoySport=False #correct
print("enjoy sport:",john.enjoySport)

#ex add docstring
'''class Pet():
    """
    a class to capture userfull information regarding my pets, ...
    """
    isHuman=False
    owner="Michael Smith"

chubbles=Pet()
print("chubble is human:",chubbles.isHuman)
print("owner :",chubbles.owner)
print(chubbles.__doc__)'''

#ex __init__方法，當用類別初始化一個物件時，它會被呼叫。
class Pet():
    """
    a class to capture userfull information regarding my pets, ...
    """
    def __init__(self,height):
        self.height=height
    
    isHuman=False
    owner="Michael Smith"

chubbles=Pet(5)
#chubbles=Pet(height=5) #correct, use key args
print("chubble height:",chubbles.height)

#ex key args with default value
class Country():
    def __init__(self,name="unspecified",population=None,sizeKmsq=None):
        self.name=name
        self.population=population
        self.sizeKmsq=sizeKmsq

usa=Country(name='United State of America',sizeKmsq=9.8e6)
#查看物件的特性清單
print("dict: ",usa.__dict__)