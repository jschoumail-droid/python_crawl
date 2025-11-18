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