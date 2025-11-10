t1=(1,2,3,4,5,6)
t2=(1,'joe',5.5)
t3=tuple(["tom","mary","joe"])
t4=tuple('python')
print(t1)
print(t2,t3)
print(t4)
print('t4= '+str(t4))
print(t1[-2])
print('method count: ',t3.count('mary'))
print('method index: ',t3.index('joe'))

for e in t1:
    print(e,end=' ')
print()

t_mixed='apple',True,3
print(t_mixed)

t_shoppinf=('apple',3),('orange',2),('banana',5)
print(t_shoppinf)