import numpy as np

matriz = np.array([[1, -1, 2], [3, 2, 0]])
print(matriz)
matriz1 = np.array([[1], [2], [3]])  # matriz de una unica columna
print(np.transpose(matriz1))
matriz2 = np.array([[1, 2, 3]])
print(np.transpose(matriz2))
print("")
print("")

"""
SISTEMAS DE ECUACIONES

Ax = B donde A=[[2,1,-2],[3,0,1],[1,1,-1]]  B=[[-3],[5],[-2]]
"""
A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
B = np.array([[-3],[5],[-2]])
print(A)
print(B)
print("")

x = np.linalg.solve(A, B)
print(x)
print("")

"""
SISTEMAS DE ECUACIONES

2x + 7y + 3z = 1
2x + 8y + 2z = 1
 x + 3y +  z = 0
"""
m1 = np.array([[2,7,3],[2,8,2],[1,3,1]])
print(m1)
m2 = np.array([1,1,0])
m2.shape=(3,1)  # da forma a la matriz, 3 filas y 1 columna
print(m2)
print(np.linalg.solve(m1, m2))