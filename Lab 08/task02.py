import numpy as np

arr = np.arange(1, 19, 2).reshape(3,3)

print(arr)

for row in arr:
    for element in row:
        print(element)
