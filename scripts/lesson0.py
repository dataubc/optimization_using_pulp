from pulp import *

# maximize x + y
# x +2y = 8
# 2x +y =7

model = LpProblem(name='small-problem', sense=LpMaximize)
# initialize descion variables
x = LpVariable(name='x', lowBound=0)
y = LpVariable(name='y', lowBound=0)

expression = x + y

model += (2 * x + y <= 8, 'red')
model += (x + 2 * y <= 7, 'green')
model += (x + y)

model.solve()

for var in model.variables():
    print(f"{var.name}: {var.value()}")

