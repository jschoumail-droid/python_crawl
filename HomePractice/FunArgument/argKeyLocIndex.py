from argKeywordLocation import convertUsdToAud

def convertAndSumList(usdList,rate=0.75):
    total=0
    for amount in usdList:
        total+=convertUsdToAud(amount,rate=rate)
    return total

def convertAndSumListKwarg(usdList,**kwargs):
    total=0
    for amount in usdList:
        total+=convertUsdToAud(amount,**kwargs)
    return total

print(convertAndSumList([1,3]))
print('kwarg: ',convertAndSumListKwarg([1,3],rate=0.8))