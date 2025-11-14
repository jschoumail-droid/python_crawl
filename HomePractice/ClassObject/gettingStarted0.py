#ex1
'''class Animal0():
    name="小鳥" #public attribute
    def sing(self):
        print("很會唱歌")

bird=Animal0()
#bird.name='birds' #correct
print(bird.name)
bird.sing()'''

#ex2
'''class Animal1():
    def __init__(self,name):
        self.name=name #public attribute，可由arg設定
    def sing(self): #public method
        print(self.name+",很會唱歌")

bird=Animal1("鸚鵡")
#bird.name='birds' #correct
print(bird.name)
bird.sing()'''

#ex3
'''class Animal2():
    def __init__(self,name,age):
        self.name=name #public attribute,可由arg設定
        self.age=age #public attribute,可由arg設定
    def sing(self): #public method
        print(self.name+str(self.age)+"歲,很會唱歌")
    def grow(self,year): #public method
        self.age+=year

bird=Animal2("鸚鵡",1)
print(bird.name)
bird.grow(1)
#bird.age=-1
bird.sing()'''

#ex3
class Animal3():
    def __init__(self,name,age):
        self.__name=name #private attribute，可由arg設定
        self.__age=age #private attribute，可由arg設定
    def __sing(self): #private method
        print(self.__name+str(self.__age),end="歲,很會唱歌")
    def talk(self): #public method
        self.__sing()
        print("會說話!")

bird=Animal3("鸚鵡",2)
#print(bird.name) #private attribute，錯誤呼叫，會產生錯誤
bird.talk()

bird.__age=-1 #private attribute，無效設定，但未產生錯誤
bird.talk()
#bird.__sing() #private method，錯誤呼叫，會產生錯誤