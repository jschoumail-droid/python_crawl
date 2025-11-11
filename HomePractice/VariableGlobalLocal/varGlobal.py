#python =(assignment) 包含C語言的定義宣告的意義，
#  若在函式內此變數未執行assignment(=)，則此變數非區域變數，其參考外部總體變數，
#     若函式外部亦未執行assignment(=)，則發生錯誤。
#  若在函式內此變數已執行assignment(=)，則此變數為區域變數,
#     若此變數以global關鍵字宣告，則此變數為總體變數

x=5
def doThings():
    print('in:',x) #函式內此變數未執行assignment(=)，此變數為總體變數

def myFunction():
    x=3
    print('in:',x) #函式內此變數x已執行assignment(=)，又未以global關鍵字宣告，此變數為local變數

score=0
def updateScore(newScore):
    score=newScore #函式內此變數score已執行assignment(=)，又未以global關鍵字宣告，此變數為local變數

score1=0
def updateScore1(newScore):
    global score1
    score1=newScore #函式內此變數score雖已執行assignment(=)，但以global關鍵字宣告，此變數為global變數

x1=4
def myFunction1():
    x1=3
    def inner():
        nonlocal x1 #宣告x1為nonlocal變數，則參考外層變數x1，此外曾變數x1可能是 global 或 local 變數
        print('inner x1:',x1)
    inner()

doThings()
print('out x:',x)
myFunction()
print('out x:',x)

updateScore(100)
print('out score:',score)

updateScore1(100)
print('out score1:',score1)

myFunction1()
print('out x1:',x1)