from pulp import *

# 定义原料和工厂
raw_materials = ['A', 'B']
factories = ['F1', 'F2']

# 定义运输成本
transport_costs = {
    ('A', 'F1'): 5000,
    ('A', 'F2'): 7000,
    ('B', 'F1'): 6000,
    ('B', 'F2'): 4000
}

# 定义工厂产能和市场需求
factory_capacity = {
    'F1': 4000,
    'F2': 6000
}

market_demand = {
    'A': 5000,
    'B': 5000
}

# 创建一个线性规划问题
prob = LpProblem('Transportation', LpMinimize)

# 定义变量
#使用 LpVariable.dicts() 函数创建了一个名为 variables 的变量字典，其中每个变量的名称由字符串 'Shipments' 和元组 (i, j) 组成，其中 i 表示原料，j 表示工厂。这个变量字典中的每个变量都是一个整数类型的变量，其取值范围大于等于 0。
variables = LpVariable.dicts('Shipments', [(i, j) for i in raw_materials for j in factories], lowBound=0, cat='Integer')

# 定义目标函数
prob += lpSum([transport_costs[(i, j)] * variables[(i, j)] for i in raw_materials for j in factories])

# 添加约束条件
for i in raw_materials:
    prob += lpSum([variables[(i, j)] for j in factories]) == market_demand[i]
    
for j in factories:
    prob += lpSum([variables[(i, j)] for i in raw_materials]) <= factory_capacity[j]

# 求解问题
prob.solve()

# 输出结果
print('Total Cost = ', value(prob.objective))
for i in raw_materials:
    for j in factories:
        print('Shipment from', i, 'to', j, '=', variables[(i, j)].varValue)