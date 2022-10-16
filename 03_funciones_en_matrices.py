import numpy as np

matriz = np.arange(20).reshape(4,5) # arange = elementos que tiene la matriz
                                    # reshape tamaño de la matriz (4 x 5)
print(matriz)
print(matriz.shape) # .shape muestra las filas y columnas de una matriz
print(matriz.ndim)  # .ndim muestra las dimensiones de una matriz
print(matriz.size)  # .size muestra el numero de elementos en la matriz

matriz_zeros = np.zeros((3, 4)) # matriz de zeros X*Y
print(matriz_zeros)

matriz_linspace = np.linspace(1, 10, 25)    # .linspace(prim elem, seg elem, num elem)
print(matriz_linspace)

matriz_3d = np.arange(24).reshape(2, 3, 4)  # .reshape(dimension, fila, columna)
print(matriz_3d)