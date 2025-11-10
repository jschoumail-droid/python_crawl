import math

def caculate(numbers):
    return(sum(math.factorial(n) for n in numbers))

numbers=[5,7,11]
#result=sum(math.factorial(n) for n in numbers)
#print(result)
#print(sum(math.factorial(n) for n in numbers))

print(caculate(numbers))