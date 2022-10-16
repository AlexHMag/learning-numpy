import numpy as np

matriz = np.array([[0, 1, 2],[5, 6, 7]])
print(matriz)
print("")
print(np.sum(matriz, axis=0))   # suma vertical, axis=1 seria horizontal

m1 = np.array([[1, 1], [1, 1]])
m2 = np.array([[5, 5], [5, 5]])
print("")
print(np.concatenate([m1, m2], axis=0))
print(np.concatenate([m1, m2], axis=1))