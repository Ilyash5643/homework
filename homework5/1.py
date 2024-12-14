import numpy as np

def mat(matrix1, matrix2):
    return matrix1.dot(matrix2)

print(mat(np.array([1, 2, 3]), np.array([[1], [2], [3]])))