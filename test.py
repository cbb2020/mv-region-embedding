import numpy as np
k = 2
arr = np.array([[1, 1, 2, 3], [3, 2, 7, 1], [6, 9, 4, 7], [2, 2, 3, 1]])
print(arr)
for i in range(4):
    print('i: ', i)
    arr[np.argsort(arr[:, i])[:-k], i] = 0
    print('column: \n', arr)
    arr[i, np.argsort(arr[i, :])[:-k]] = 0
    print('row: \n', arr)

# print(arr.shape)
# print(arr)