import numpy as np

array = np.arange(1, 101)
chetnye = array[array % 2 == 0]
sum = np.sum(chetnye)
print(sum)
