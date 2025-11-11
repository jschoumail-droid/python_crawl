#Fn=Fn-1+Fn-2，其中 F0=0 和 F1=1

def fibonacciRecursion(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacciRecursion(n-2)+fibonacciRecursion(n-1)

num=10
print('fibonacci(%d)=%d' % (num,fibonacciRecursion(num)))