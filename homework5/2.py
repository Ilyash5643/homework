import numpy as np

def err(y1, y2):
    y1 = np.array(y1)
    y2 = np.array(y2)
    mse = np.mean((y1 - y2) ** 2)
    return mse

y1 = [4, 3, 2, 1]
y2 = [1, 2, 3, 4]

print(err(y1, y2))
