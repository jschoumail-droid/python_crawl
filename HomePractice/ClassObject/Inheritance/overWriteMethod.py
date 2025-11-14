class Person():
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    
    @property
    def fullName(self):
        return '%s %s' % (self.firstName,self.lastName)
    
    @fullName.setter
    def fullName(self,name):
        first,last=name.split(' ')
        self.firstName=first
        self.lastName=last
    
myPerson=Person('Mary','Smith')
print('Person:',myPerson.fullName)
#如下設定，即產生錯誤，修改如下:
#myPerson.fullName='Mary Anne  Smith'

class BetterPerson(Person):
    @property
    def fullName(self):
        return '%s %s' % (self.firstName,self.lastName)
    
    @fullName.setter
    def fullName(self,name):
        names=name.split(' ')
        self.firstName=names[0]
        if len(names)>2:
            self.lastName=' '.join(names[1:])
        elif len(names)==2:
            self.lastName=names[1]

myPerson1=BetterPerson('Mary','Smith')
myPerson1.fullName='Mart Anne Smith'
print('Better Person:',myPerson1.firstName)
print(myPerson1.lastName)