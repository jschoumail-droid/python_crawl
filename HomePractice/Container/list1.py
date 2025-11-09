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

