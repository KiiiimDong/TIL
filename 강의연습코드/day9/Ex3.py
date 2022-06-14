import numpy as np
from numpy.linalg import inv
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).reshape((3,3))
print(A)
print(inv(A))

#2x - y = 0
#x + y = 3
#Y=WX
#W = YX^-1
X = np.array([[2, -1], [1, 1]])
Y = np.array([[0], [3]])
inv_X = inv(X)
print(Y.shape)
print(inv_X.shape)
W = inv_X.dot(Y)
print(W)
