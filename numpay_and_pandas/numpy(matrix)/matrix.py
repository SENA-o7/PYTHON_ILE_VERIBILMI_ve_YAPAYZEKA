import numpy as np
matrix=np.random.randint(1,10,size=(3,3))
tmatrix=matrix.T
dmatrix=np.linalg.det(matrix)
matrix_carpma=matrix*2

print("Asıl matrix:\n",matrix)
print("---------------------")
print("Transpose matrix:\n ",tmatrix)
print("---------------------")
print("Determinant:\n ",dmatrix)
print("---------------------")
print("2 ile çarpılmış matrix:\n",matrix_carpma)

