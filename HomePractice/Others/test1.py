class Circle():
    isShape=True
    def __init__(self,radius,color='red'):
        self.radius=radius
        self.color=color

firstCircle=Circle(2,'blue')
secondCircle=Circle(3)

print(firstCircle.color,secondCircle.color)
print(firstCircle.__dict__)

print('------------------')
def primes_below(bound):
    candidates=list(range(2,bound))
    while len(candidates)>0:
        yield candidates[0]
        candidates=[c for c in candidates if c%candidates[0]!=0]

print([prime for prime in primes_below(100)])

powers = (x**2 for x in range(100))

for x in powers:
    print(x)

def yield_test(n):
    print("start n =", n)
    for i in range(n):
        yield i*i
        print("i =", i)

    print("end")

tests = yield_test(5)
for test in tests:
    print("test =", test)
    print("--------")

print('=======')
def test():
    print("start...")
    while True:
        throw = yield 10
        print("throw:", throw)

p = test()
print(next(p))
print("-----------")
print(next(p))
print("-----------")
print(p.send(7))
print("-----------")