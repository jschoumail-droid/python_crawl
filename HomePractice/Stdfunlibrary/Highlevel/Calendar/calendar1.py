#ex1
print('=====ex1=====')
import calendar

c=calendar.Calendar()
print(c)
print(c.itermonthdates(2025,11))
print(list(c.itermonthdates(2025,11)))
#for i in list(c.itermonthdates(2025,11)):
#    print(i)
lst=list(d for d in c.itermonthdates(2025,11) if d.month==11)
for i in lst:
    print(i)
