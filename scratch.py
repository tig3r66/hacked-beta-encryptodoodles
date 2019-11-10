import numpy as np

matrix = ([
    [42, 42, 25, 35],
    [31, 45, 19, 40],
    [19, 34, 13, 35],
    [27, 26, 13, 30]
])

inverse_matrix = ([
    [-4/35, 3/35, -11/35, 17/35],
    [17/35, -4/35, 3/35, -11/35],
    [-11/35, 17/35, -4/35, 3/35],
    [3/35, -11/35, 17/35, -4/35]
])

res = np.dot(inverse_matrix, matrix)
res = res.astype(int)
print(res)
