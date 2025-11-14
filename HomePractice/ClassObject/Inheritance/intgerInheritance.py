class MyInt(int):
    def isDivisibleBy(self,x):
        return self%x==0
    
a=MyInt(8)
print(a)
print(a.isDivisibleBy(2))