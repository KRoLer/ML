import numpy as np
from past.builtins import xrange

X = np.array([[1, 1, 1, 1],
              [2, 2, 2, 2],
              [3, 3, 3, 3],
              [3, 3, 3, 3]])

T = np.array([[4, 4, 4, 4],
              [5, 5, 5, 5],
              [6, 6, 6, 6],
              [6, 6, 6, 6]])
# print("X:")
# print(X)
# print("Test")
# print(T)

# dists = np.zeros()

sum = np.dot(X, T.T)
sumX = np.dot(X, T.T).T
# print(sum)
# print(sumX)

# print(X[0,0])
# arr = [1,2,3,4,5]
# print(np.delete(X, [0, len(X[:])-1], axis=1))

print("Normal: ", np.dot(X, T))
print("T.T: ", np.dot(X, T.T))
