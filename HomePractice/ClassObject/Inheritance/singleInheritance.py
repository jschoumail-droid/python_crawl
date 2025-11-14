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
