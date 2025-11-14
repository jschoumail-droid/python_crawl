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