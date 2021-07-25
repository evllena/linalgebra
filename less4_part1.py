import numpy as np


def is_valid(x, x_ext):
    if np.linalg.matrix_rank(x) == np.linalg.matrix_rank(x_ext) and np.linalg.matrix_rank(x_ext) != len(x_ext[0]):
        print("Система совместна и имеет одно решение.")
    else:
        print('Система несовместна.')


print("2A:")
A = np.array([[3, -1, 1], [2, -5, -3], [1, 1, -3]])
A1 = np.array([4, -17, 0])
A_ext = np.array([[3, -1, 1, 4], [2, -5, -3, -17], [1, 1, -3, 0]])
is_valid(A, A_ext)
print(np.linalg.solve(A, A1))

print("2Б:")
B_ext = np.array([[2, -4, 6, 1], [1, -2, 3, -2], [3, -6, 9, 5]])
B = np.array([[2, -4, 6], [1, -2, 3], [3, -6, 9]])
is_valid(B, B_ext)


print("2B:")
C_ext = np.array([[1, 2, 5, 4], [3, 1, -8, -2]])
C = np.array([[1, 2, 5], [3, 1, -8]])
is_valid(C, C_ext)


print("3:")
D_ext = np.array([[1, 3, -2, 4, 3], [0, 5, 0, 1, 2], [0, 0, 3, 0, 4],[0, 0, 0, 2, 1]])
D = np.array([[1, 3, -2, 4], [0, 5, 0, 1], [0, 0, 3, 0], [0, 0, 0, 2]])

if np.linalg.matrix_rank(D) == np.linalg.matrix_rank(D_ext):
    print("Система совместна и имеет одно решение.")
else:
    print('Система несовместна.')

print("4:")
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

a = [i for i in range(0, 2)]
b = [i for i in range(0, 2)]
c = [i for i in range(0, 2)]

for aa in a:
    for bb in b:
        for cc in c:
            M_ext = np.array([[1, 2, 3, aa], [4, 5, 6, bb], [7, 8, 9, cc]])
            if np.linalg.matrix_rank(M) != np.linalg.matrix_rank(M_ext):
                answer = np.array([aa, bb, cc])
                print(answer)

print('Система несовместна при a!=b!=c')

