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
