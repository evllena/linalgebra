import numpy as np

np.set_printoptions(precision=2, suppress=True)

A = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 2], [1, 6, 5], [0, 1, 0]])

U, s, W = np.linalg.svd(A)

V = W.T
D = np.zeros_like(A, dtype=float)
D[np.diag_indices(min(A.shape))] = s

print(f'Матрица D:\n{D}')
print(f'Матрица U:\n{U}')
print("Убедимся в ортогональности матрицы U:")
print(np.dot(U.T, U))
print(f'Матрица V:\n{V}')
print("Убедимся в ортогональности матрицы V:")
print(np.dot(V.T, V))
print("Проверка:")
print(f'{np.dot(np.dot(U, D), V.T)}')

print(f'Матрица A:\n{A}')

print(f"Норма Фробениуса - {np.linalg.norm(A, ord='fro')}")
print(f"Евклидова норма - {np.linalg.norm(np.reshape(A, newshape=(15,1)))}")