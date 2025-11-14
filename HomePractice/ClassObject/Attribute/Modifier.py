#Attribute modifiers

#ex 未加 Attribute modifiers
class Temperature():
    def __init__(self,celsius):
        self.celsius=celsius

    def fahrenheit(self):
        return self.celsius*9/5+32
    
myTemp=Temperature(0)
print(myTemp.fahrenheit()) #fahrenheit()必須有括號
myTemp=Temperature(-10)
print(myTemp.fahrenheit())

#ex 加上 Attribute modifiers
class Temperature1():
    def __init__(self,celsius):
        self.celsius=celsius
    @property #加上 Attribute modifiers，呼叫時視為屬性，故不需加括號
    def fahrenheit(self):
        return self.celsius*9/5+32
    
    @fahrenheit.setter
    def fahrenheit(self,value):
        if value<-460:
            raise ValueError('Temperature less than -460F are not possible')
        self.celsius=(value-32)*5/9
    
myTemp1=Temperature1(0)
print('add modifier :',myTemp1.fahrenheit) #fahrenheit 不需括號
myTemp1=Temperature1(-10)
print('add modifier :',myTemp1.fahrenheit)
#myTemp1.fahrenheit=-500

#ex 
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
    
customer=Person('Mary','Lou')
print(customer.fullName)

# error, 未加入@fullName.setter修飾詞時，fullname是方法，不能當屬性來設定
#customer.fullName='Mary Schmidt'

#correct, 加入@fullName.setter修飾詞及fullName(self,name)方法時，此statement是執行fullName(self,name)方法
customer.fullName='Mary Schmidt'
print(customer.lastName)