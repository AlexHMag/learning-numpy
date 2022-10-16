import numpy as np

matriz = np.arange(24).reshape(4, 6)
print(matriz)
print(matriz[3, 4]) # ubicacion del elemento

matriz_1d = np.array([2, 5, 6, 9, 3, 6, 7, 1])
print(np.sort(matriz_1d))  # .sort ordena los elementos en la matriz de forma ascendente
print(np.power(matriz_1d, 3))   # .power eleva los elementos al numero designado
print(np.array(matriz_1d**3))   # manera simplificada de .power
print(np.array(matriz_1d.max()))    # busca el maximo
print(np.array(matriz_1d.min()))    # busca el minimo

m1 = [1, 2, 3]
m2 = [11, 22, 33]
print(np.concatenate((m1, m2)))   # une las dos matrices en una sola

m1_2d = np.array([[1, 2], [3, 4]])
m2_2d = np.array([[5, 6], [7, 8]])
print(m1_2d + m2_2d)
print(m1_2d + 2)
print(np.add(m1_2d, m2_2d)) # igual que la suma pero usando funcion
print(np.subtract(m1_2d, m2_2d)) # resta
print(np.multiply(m1_2d, m2_2d)) # multiplicacion
print(np.divide(m1_2d, m2_2d)) # division