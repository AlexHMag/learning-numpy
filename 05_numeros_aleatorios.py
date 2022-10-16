import numpy as np

# No son resultados aleatorios.
# Aleatorio significa que no se puede predecir logicamente.

matriz = np.random.randint(10, size=(5))    # 5 numero aleatorios
matriz_2d = np.random.randint(10, size=(3, 3)) # matriz 3*3 de numeros aleatorios
print(matriz)

matriz_extraer = np.random.choice([5, 2, 7, 9], size=(2, 3)) # devuelve uno de los valores de la matriz
print(matriz_extraer)

"""
EJERCICIO
Genere una matriz que contenga 50 valores, donde
cada valor debe ser 2, 4, 8 o 10.
"""

m = np.random.choice([2, 4, 8, 10], p = [0.25, 0.25, 0.25, 0.25], size=(50))
print(m)