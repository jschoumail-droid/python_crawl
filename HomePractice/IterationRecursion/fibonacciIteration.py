#Fn=Fn-1+Fn-2，其中 F0=0 和 F1=1

def fibonacciItetation(n):
    previous=0
    current=1

    for i in range(n-1):
        currentOld=current
        current += previous
        previous=currentOld
    return current

num=3
print('fibonacci(%d)=%d' % (num,fibonacciItetation(num)))