import numpy as np

matrix = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
t_mat = np.transpose(matrix)
sun_mat = np.sum(t_mat)
print(t_mat)
print(sun_mat)