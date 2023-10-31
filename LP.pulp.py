# Maximize  f(x) = 2x1 + 3x2

# Subject to:
#             -x1 + x2 <= 1
#             x1 + x2 >= 2
#             x2 >= 0

import pulp as pulp

# 创建一个LP问题实例，求解最大化目标函数
problem = pulp.LpProblem("LP problem", pulp.LpMaximize)

# 创建决策变量 x1 和 x2，取值范围为非负实数
x1 = pulp.LpVariable("x1", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Continuous')

# 添加目标函数和约束条件
problem += 2*x1 + 3*x2, "Objective Function"
problem += -x1 + x2 <= 1, "Constraint 1"
problem += x1 + x2 >= 2, "Constraint 2"
problem += x2 >= 0, "Constraint 3"

# 求解LP问题
status = problem.solve()

# 输出结果
print("Status:", pulp.LpStatus[status])
print("Maximum value of f(x):", pulp.value(problem.objective))
print("x1:", pulp.value(x1))
print("x2:", pulp.value(x2))