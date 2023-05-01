import numpy as np


m1 = np.array([
    [0,1,1,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,1,1,0],
])
m2 = np.array([
    [0,1,1,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,1,1,0],
])

print(np.matmul(np.matmul(np.matmul(np.bool_(m1),np.bool_(m2)),np.bool_(m2)),np.bool_(m2)))