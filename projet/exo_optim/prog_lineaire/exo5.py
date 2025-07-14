import numpy as np
from scipy.optimize import linprog
#multiplié par -1 car c'est un problème de maximisation, pour avoir un problème de minimisation
# Coefficients de l'objectif
c = np.array([-3, -2, 0, 0, 0]) # -Z = -3x - 2y

# Coefficients des contraintes
#Dans ce cas, nous avons trois contraintes : x + y + s1 = 4 x + s2 = 2 y + s3 = 3

A = np.array([[1, 1, 1, 0, 0], #x + y + s1 = 4
               [1, 0, 0, 1, 0], #  x + s2 = 2
                 [0, 1, 0, 0, 1]]) # y + s3 = 3

#deuxieme membre des contraintes
b = np.array([4, 2, 3])

# Résolution du problème
res = linprog(c, A_ub=A, b_ub=b)

# Affichage de la solution
print("Valeur optimale de x : ", res.x[0])
print("Valeur optimale de y : ", res.x[1])

# Notez que la fonction linprog retourne la valeur optimale de l'objectif, 
# qui est la valeur minimale de -Z. Pour obtenir la valeur maximale de Z, 
# nous devons multiplier cette valeur par -1.
print("Valeur optimale de l'objectif : ", -res.fun)