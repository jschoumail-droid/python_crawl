# map(欲直行的function名稱, 可迭代物件的名稱)
# map回傳一個生成器物件，可以將它轉換成list

names=['Magda','Jose','Anne']

#method 1
lengths=[]
for name in names:
    lengths.append(len(name))

print(lengths)
print('average length=',sum(lengths)/len(lengths))

#method 2
lengths1=[]
lengths1=list(map(len,names))

print(lengths1)
print('average length=',sum(lengths1)/len(lengths1))
            