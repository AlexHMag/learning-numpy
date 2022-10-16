import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)
print("")
print(np.amax(matriz, 0))   # valor maximo de todas las columnas, axis=0
print(np.amin(matriz, 1))   # valor minimo de todas las filas, axis=1

print("")
print(np.ptp(matriz, axis=1))    #rango = max - min
print(np.percentile(matriz, 50, axis=1))    # percentil = (q(n+1))/100, --> q=50
                                            # q=percentil a calcular(0-100), n=total datos
                                            # si n=PAR: percentil=(q*n)/100
print(np.median(matriz, axis=1))    # mediana de cada fila
print(np.mean(matriz, axis=0))  # media de las columnas
print(np.std(matriz))   # desviacion escandar