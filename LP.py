# Maximize  f(x) = 2x1 + 3x2

# Subject to:
#             -x1 + x2 <= 1
#             x1 + x2 >= 2
#             x2 >= 0
import numpy as np
from scipy.optimize import linprog

c = [-2, -3]

# 定义约束条件系数矩阵 A 和约束条件右侧常数 b
A = [[-1, 1], [1, 1], [0, 1]]
b = [1, 2, 0]

# 定义每个决策变量的取值范围
x0_bounds = (None, None)
x1_bounds = (0, None)
bounds = [x0_bounds, x1_bounds]

# 使用 linprog 函数求解线性规划问题
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds)

# 输出结果
print(res)