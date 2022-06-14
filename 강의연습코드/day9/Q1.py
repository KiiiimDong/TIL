import numpy as np
from numpy.linalg import inv
a = np.array([[2, 3], [1, -2]])
b = np.array([[1], [4]])
print(inv(a).dot(b))