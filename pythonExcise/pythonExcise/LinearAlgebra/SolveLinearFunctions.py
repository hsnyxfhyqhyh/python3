import numpy as np
from scipy.linalg import solve

'''
线性方程组： 

2x_1 + 2x_2 - x_3 + x_4 = 4
4x_1 + 3x_2 - x_3 + 2x_4 = 6
8x_1 + 5x_2 - 3x_3 + 4x_4 = 12
3x_1 + 3x_2 - 2x_3 - 2x_4 = 6

'''
a = np.array([[2, 2, -1, 1], [4, 3, -1, 2], [8, 5, -3, 4], [3, 3, -2, -2]])
b = np.array([4, 6, 12, 6])

x = solve(a, b)
print(x)    #x_1= 3/7, x_2 = 1, x_3 = -1, x_4 = 1/7