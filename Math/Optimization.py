from pulp import *

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0', pulp.const.LpMaximize)
problem += 0.5*x1 + 300*x2, "Функция цели"
problem += x1 + 90*x2 <= 10000, "1"
problem += x2 <= 20, "2"
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Прибыль:")
print (value(problem.objective))