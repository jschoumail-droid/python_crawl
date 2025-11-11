def add_suffix(sufix='.com'):
    return 'google'+sufix

if __name__ =='__main__':
    print(add_suffix())
    print(add_suffix('.co.uk'))

def convertUsdToAud(amount,rate=0.75):
    return amount/rate

def convertCurrency(amount,rate,margin=0):
    return amount*rate*(1+margin)

def computeUsdTotal(amountInAud=0,amountIngbp=0):
    total=0
    total+=convertCurrency(amountInAud,0.78)
    total+=convertCurrency(amountIngbp,1.29,0.01)
    return total

if __name__ =='__main__':
    print(convertUsdToAud(100))
    print(convertUsdToAud(100,0.78))
    print(computeUsdTotal(amountIngbp=10))