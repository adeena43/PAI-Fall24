import numpy as np
import random

matrix1 = np.random.randint(1, 10, size = (5, 3))
matrix2 = np.random.randint(1, 10, size = (3, 2))

print(matrix1)
print(matrix2)

resultant = matrix1*matrix2
print(resultant)

#this program generates the following error
#ValueError: operands could not be broadcast together with shapes (5,3) (3,2)
