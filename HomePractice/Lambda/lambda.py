#lambda 僅適用於1行的函式
# lambda arguments : expression

'''def addUp(x,y):
    return x+y'''

addUp = lambda x,y:x+y

print(addUp(2,5))

firstItem=lambda myList:myList[0]

print(firstItem(['cat','dog','mouse']))