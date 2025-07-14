#maximiser Z=3x+2y
#sujet aux contraintes
#x+y<=4
#2x+y<=5
#x,y appartient a N

from pulp import LpProblem, LpVariable, LpMaximize, LpInteger

prob = LpProblem("Test", LpMaximize)

x = LpVariable("x", lowBound=0, cat=LpInteger)
y = LpVariable("y", lowBound=0, cat=LpInteger)

prob += 3*x + 2*y #fonction objectif

prob += x + y <= 4 #contraintes 1
prob += 2*x + y <= 5 #contraintes 2

prob.solve()

print(f"Status : {prob.status}")
print("Valeur optimale de x : ", x.value())
print("Valeur optimale de y : ", y.value())
print("Valeur optimale de Z : ", prob.objective.value())