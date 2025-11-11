def countDown(n):
    if n==0:
        print('listoff')
    else:
        print(n)
        return countDown(n-1)
    
def factorialRecursion(n):
    if n==1:
        return 1
    else:
        return n*factorialRecursion(n-1)
    
countDown(3)
num=5
print('factorial(%d)=%d' % (num,factorialRecursion(num)))