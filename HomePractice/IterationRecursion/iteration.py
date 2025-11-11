def sumFirstN(n):
    result=0
    for i in range(1,n+1):
        result+=i
    return result

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def factorialIteration(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result


print(sumFirstN(100))
num=7
print('num={} is prime:{}'.format(num,isPrime(num)))
num1=5
print('factorial(%d)=%d' % (num1,factorialIteration(num1)))
