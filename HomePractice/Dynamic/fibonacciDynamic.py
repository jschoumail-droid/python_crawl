stored={0:0,1:1}

def fibonacciDynamic(n):
    if n in stored:
        return stored[n]
    else:
        stored[n]=fibonacciDynamic(n-2)+fibonacciDynamic(n-1)
        return stored[n]

num=100
print('fibonacciDynamic(%d)=%d' % (num,fibonacciDynamic(num)))