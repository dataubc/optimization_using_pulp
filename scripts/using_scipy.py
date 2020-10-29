from scipy.optimize import linprog


# max x + y, the default is to minimize so if you want to maximize then you have to a take the negative
c = [-1,-1]


# the equations are
# 2x + y <= 8
# x + 2y <= 7

A = [[2,1],[1,2]]
b = [8,7]

# let's define the bounds
x0_bounds = [0,100]
x1_bounds = [0,100]

res = linprog(c,A_ub=A,b_ub=b,bounds = [x0_bounds,x1_bounds])
print(res)
