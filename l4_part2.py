import numpy as np
import scipy.linalg as la

print("TASK 2A:")
A = np.array([[1, 2, 4], [2, 9, 12], [3, 26, 30]])
P, L, U = la.lu(A)
print(L)

print("TASK 2Б:")
A = np.array([[1, 1, 2, 4], [2, 5, 8, 9], [3, 18, 29, 18], [4, 22, 53, 33]])
P, L, U = la.lu(A)
print(L)

print("TASK 3:")
A = np.array([[2, 1, 3], [11, 7, 5], [9, 8, 4]])
B = np.array([[1, -6, -5]])
P, L, U = la.lu(A)
C = np.concatenate((A, B.T), axis=1)
B = np.array([1, -6, -5])
answer = np.linalg.solve(A, B)

print(f'x1 = {answer[0]}, x2 = {answer[1]}, x3 = {answer[2]}')

print("TASK 4:")
A = np.array([[81, -45, 45], [-45, 50, -15], [45, -15, 38]])
B = np.array([531, -460, 193])
L = np.linalg.cholesky(A)
LT = np.transpose(L)
y = np.linalg.solve(L, B)
x = np.linalg.solve(LT, y)

print(f'x1 = {x[0]}, x2 = {x[1]}, x3 = {x[2]}')
