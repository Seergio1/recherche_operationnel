# Voici la formulation du problème :

# Maximiser l'utilisation des ressources du data center en affectant les tâches CPU et I/O aux ressources disponibles.

# Variables :

# x : nombre de tâches CPU à affecter
# y : nombre de tâches I/O à affecter
# Contraintes :

# 3x + 2y ≤ 18 (capacité CPU)
# x + 2y ≤ 12 (capacité I/O)
# x ≥ 0 (nombre de tâches CPU non négatif)
# y ≥ 0 (nombre de tâches I/O non négatif)
# Objectif :
# Maximiser le gain : 5x + 4y

import numpy as np
from scipy.optimize import linprog

# Coefficients de l'objectif
c = np.array([-5, -4])  # Coefficients de x et y (gain)

# Coefficients des contraintes
A = np.array([[3, 2], [1, 2]])  # Coefficients de x et y pour les contraintes
b = np.array([18, 12])  # Valeurs des contraintes

# Résolution du problème de programmation linéaire
res = linprog(c, A_ub=A, b_ub=b)

# Affichage de la solution
print("Nombre de tâches CPU à affecter : ", res.x[0])
print("Nombre de tâches I/O à affecter : ", res.x[1])
print("Gain maximal : ", -res.fun)

