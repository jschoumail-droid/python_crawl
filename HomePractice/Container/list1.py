'''list1=['a',2,{3,4}]
print(list1)
b=1.0/3.0
print("b=%7.2f" % (b))'''
#remark1

m=[[1,2,3],[4,5,6]]
for row in m:
    for col in row:
        print(col,end="")        
print()

for i in range(len(m)):
    for j in range(len(m[1])):
        print(m[i][j],end="")
print()

X=[[1,2,3],[4,5,6],[7,8,9]]
Y=[[10,11,12],[13,14,15],[16,17,18]]
result=[[0]*len(X[0]) for row in range(len(X))]
print(X,Y,result)

#add
'''for row in range(len(X)):
    for col in range(len(X[0])):
        result[row][col]=X[row][col]+Y[row][col]
print(result)'''
#multiply
for row in range(len(X)):
    for col in range(len(Y[0])):
        for index in range(len(Y)):
            result[row][col]+=X[row][index]*Y[index][col]
print(result)
