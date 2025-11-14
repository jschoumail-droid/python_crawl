import datetime

class MyDate(datetime.date):
    def addDays(self,n):
        return self+datetime.timedelta(n)
    
d=MyDate(2025,11,1)
print(d.addDays(10))
print(d.addDays(45))