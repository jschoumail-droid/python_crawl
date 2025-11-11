n=[5,8,1,3,2]
print(n)

stillSwapping=True
while stillSwapping:
    stillSwapping=False
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]
            stillSwapping=True

print('bubble sort:',n)