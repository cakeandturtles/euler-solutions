def mMatrixR(m,n):
    matrixOne = []
    for i in range(m):
        matrixTwo = []
        for j in range(n):
            matrixTwo.append(i)
        matrixOne.append(matrixTwo)
    return matrixOne

print mMatrixR(2,2)
print
print mMatrixR(3,2)
