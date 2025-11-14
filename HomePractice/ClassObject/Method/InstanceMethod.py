import math
print()
#__init__()就是instance method
class Circle():
    isShape=True
    def __init__(self,radius,color='red'):
        self.radius=radius
        self.color=color
    def area(self):
        return math.pi*self.radius**2
    
circle=Circle(3)
print(circle.area())
print(circle.color)

class Pet():
    def __init__(self,height):
        self.height=height
    
    isHuman=False
    owner="Michael Smith"

    def isTall(self,tallIfAtLeast):
        return self.height>=tallIfAtLeast

chubbles=Pet(40)
print(chubbles.height)
print("is tall? ",chubbles.isTall(30))