
#ex1
class Animal():
    def __init__(self,name):
        self.name=name
    def fly(self):
        print(self.name+"很會飛")

class Bird(Animal):
    def __init__(self,name,age):
        super().__init__(name) #設定繼承父類別name屬性
        self.age=age
    def fly(self): #覆蓋父類別fly()方法
        print('in bird cls,',self.name) #correct
        print(str(self.age),end="歲")
        super().fly() #呼叫父類別fly()method

pigeon=Animal("小白鴿")
pigeon.fly()

parrot=Bird("小鸚鵡",2)
parrot.fly()

#ex2 使用super()呼叫父類別方法
class Person():
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

    def speak(self):
        print('Hello, my name is %s' % (self.firstName))

class TalkativePerson(Person):
    def speak(self):
        #print('Hello, my name is %s' % (self.firstName))
        super().speak()
        print('It is pleasure to meet you!')

john=TalkativePerson('John','Tomic')
john.speak()

#ex 使用super()覆寫方法

import datetime

class Diary():
    def __init__(self,birthday,christmas):
        self.birthday=birthday
        self.christmas=christmas

    @staticmethod
    def formatDate(date):
        return date.strftime('%d-%b-%y')

    def showBirthday(self):
        return self.formatDate(self.birthday)
    def showChristmas(self):
        return self.formatDate(self.christmas)
    
class CustomDiary(Diary):
    def __init__(self,birthday,christmas,dateFormat):
        self.dateFormat=dateFormat
        super().__init__(birthday,christmas)
    def formatDate(self,date):
        return date.strftime(self.dateFormat)
    
firstDay=CustomDiary(datetime.date(2025,1,1),datetime.date(2025,3,3),'%d-%b-%Y')
secondDay=CustomDiary(datetime.date(2025,1,1),datetime.date(2025,3,3),'%d/%m/%Y')

print(firstDay.showBirthday())
print(secondDay.showChristmas())