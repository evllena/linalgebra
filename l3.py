import numpy as np


# Task1
a = np.array([[-1, -6], [2, 6]])
w, v = np.linalg.eig(a)
print('TASK 1')
print(f'Собственные векторы:\n{v}')
print(f'Собственные значения:\n{w}')

# Task3

a = np.array([[1, 1], [-1, 3]])
b = np.array([[1], [1]])
z = np.dot(a, b)
print('TASK 3')
print(z)

# λ = 2, вектор b  является собственным вектором линейного оператора, заданного матрицей А

# Task4
a = np.array([[0, 3, 0], [3, 0, 0], [0, 0, 3]])
x = np.array([[3], [-3], [-4]])
z = np.dot(a, x)
print('TASK 4')
print(z)
# вектор x не является собственным вектором линейного оператора, заданного матрицей А