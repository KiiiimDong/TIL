import numpy as np
from numpy.linalg import inv
a = np.array([2, 1]) # vector 선
m1 = np.array([[1, 2], [3, 4]]) # 행렬 면
m2 = np.array([[1, 2], [3, 4]])
print(m1 + m2)
print(np.linalg.norm(a))
i_m1 = inv(m1)
print(i_m1)
print(m1*m2) # 각각의 위치에서 연산 (행렬의 곱이 아님.)
print(np.dot(m1, m2)) # 내적
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.dot(x, y))
m_x = np.array([[1, 2, 3]])
m_y = np.array([[4, 5, 6]])
print(m_x)
print(m_y)
print(m_x.shape)
print(m_y.shape)
m_y = m_y.T # 행렬의 전치 (트랜스포즈)
print(m_y)
print(m_y.shape)
print("(n, m).(m, c)")
print(np.dot(m_x, m_y))
print(m_x.dot(m_y)) # 위에거랑 똑같은 이야기.
a1 = np.array([[1, 2, 3], [-1, -2, -3]])
a2 = np.array([[4, 5, 6], [-4, -5, -6]])
a2 = a2.T
y = a1.dot(a2)
print(y)