# Trabaja con matrices n-dimensionales.
# Altamente util para calculos matematicos, data science y machine learning

# Las LISTAS tienen diferentes tipos de datos mientras que en las ARRAYs solo tendremos un
# tipo de dato

import array as arr
import numpy as np

matriz_array = arr.array('i', [1, 2, 3, 4, 5]) # i = int, d = decimalesç

print("Esto es con el ARRAY")
for numero in matriz_array:
    print(numero)

print("Esto es con NUMPY")
matriz_np = np.array([1, 2, 3, 4, 5]) # tratamos los datos como si fueran una lista
print(matriz_np)

# Diferenciacion de uso de listas y arrays
print("Diferencia uso lista/array")
lista = [1, 3, 5]
matriz_lista = np.array([2, 4, 6])

print(lista) # coleccion de datos, podemos aplicarle .append
print(matriz_lista) # coleccion de datos independientes, aqui matriz + X = cada valor+X