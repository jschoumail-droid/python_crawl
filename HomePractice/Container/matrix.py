'''#for multiply
arrA=[[1,2],[2,3],[3,4]]
arrB=[[1,2,3,4],[2,3,4,5]]'''
'''#for add
arrA=[[1,2],[2,3],[3,4]]
arrB=[[3,4],[5,6],[7,8]]'''

#pair 2
#for multiply & add
arrA=[[1,2,3],[2,3,4],[3,4,5]]
arrB=[[3,4,5],[5,6,7],[7,8,9]]

def getRowCol(A):
    intRow=len(A)
    intCol=len(A[0])
    
    return intRow,intCol

bolCanMultiply = (len(arrA[0])==len(arrB))
bolCanAdd = ((len(arrA)==len(arrB) and len(arrA[0])==len(arrB[0])))

def Multiply(A,B):
    intARow,intACol=getRowCol(A)
    intBCol =len(B[0])
    AB=[[0]*intBCol for row in range(intARow)]
    
    for i in range(intARow):
        for j in range(intBCol):
            sum=0
            for k in range(intACol):
                sum+=(A[i][k]*B[k][j])
            AB[i][j]=sum
    
    return AB

def Add(A,B):
    intARow,intACol=getRowCol(A)

    AB=[[0]*intACol for row in range(intARow)]
    
    for i in range(intARow):
        for j in range(intACol):
            AB[i][j]=A[i][j]+B[i][j]
   
    return AB

def MultiplyWColRow(A,B,intARow,intACol,intBCol):
    AB=[[0]*intBCol for row in range(intARow)]
    
    for i in range(intARow):
        for j in range(intBCol):
            sum=0
            for k in range(intACol):
                sum+=(A[i][k]*B[k][j])
            AB[i][j]=sum
    
    return AB

def AddWColRow(A,B,intARow,intACol):
    AB=[[0]*intACol for row in range(intARow)]
    
    for i in range(intARow):
        for j in range(intACol):
            AB[i][j]=A[i][j]+B[i][j]
   
    return AB

#mehod 1,僅傳入arrA,arrB, 不須傳入intarrARow,intarrACol,intarrBCol
'''if bolCanMultiply and bolCanAdd:
    arrC=Multiply(arrA,arrB)
    arrCa=Add(arrA,arrB)
elif bolCanMultiply:
    arrC=Multiply(arrA,arrB)
elif bolCanAdd:
    arrCa=Add(arrA,arrB)
else:
    print("Warning! arrA, arrB 不能相乘或相加。")'''

#mehod 2,同時傳入arrA,arrB,intarrARow,intarrACol,intarrBCol
if bolCanMultiply and bolCanAdd:
    intarrARow,intarrACol =getRowCol(arrA)
    arrCa=AddWColRow(arrA,arrB,intarrARow,intarrACol)
    
    intarrBCol=len(arrB[0])
    arrC=MultiplyWColRow(arrA,arrB,intarrARow,intarrACol,intarrBCol)

elif bolCanMultiply:
    intarrARow,intarrACol =getRowCol(arrA)
    intarrBCol=len(arrB[0])
    arrC=MultiplyWColRow(arrA,arrB,intarrARow,intarrACol,intarrBCol)
elif bolCanAdd:
    intarrARow,intarrACol =getRowCol(arrA)
    arrCa=AddWColRow(arrA,arrB,intarrARow,intarrACol)
else:
    print("Warning! arrA, arrB 不能相乘或相加。")

print("A=",arrA)
print("B=",arrB)
if bolCanMultiply and bolCanAdd:
    print("C=A*B=",arrC)
    print("C=A+B=",arrCa)
elif bolCanMultiply:
    print("C=A*B=",arrC)
elif bolCanAdd:
    print("C=A+B=",arrCa)