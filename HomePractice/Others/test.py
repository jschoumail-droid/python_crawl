'''import keyword
print(keyword.kwlist)'''
x=10
print(x.bit_length())
print(x.__doc__)
print(type(x))

class Pet():
    """A class to capture ..."""
    def __init__(self,height):
        self.height=height
    is_human=False
    owner='Mary'

happy=Pet(50)
print(type(happy))
print(happy.is_human)
print(happy.height)
print(happy.__doc__)
print(happy.owner)