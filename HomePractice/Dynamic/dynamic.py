import time

storedResults={}

def sumToN(n):
    startTime=time.perf_counter()
    result=0
    for i in reversed(range(n)):
        if i+1 in storedResults:
            print('Stopping sum at %s because we have previously computed it' % str(i+1))
            result+=storedResults[i+1]
            break
        else:
            result+=i+1
    storedResults[n]=result
    print(time.perf_counter()-startTime,'seconds')
    return result

#print(sumToN(5))
#print(sumToN(6))
print(sumToN(1000000))
print(sumToN(1000000))