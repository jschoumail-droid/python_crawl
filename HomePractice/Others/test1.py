class Circle():
    isShape=True
    def __init__(self,radius,color='red'):
        self.radius=radius
        self.color=color

firstCircle=Circle(2,'blue')
secondCircle=Circle(3)

print(firstCircle.color,secondCircle.color)
print(firstCircle.__dict__)