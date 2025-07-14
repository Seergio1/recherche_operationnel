import numpy as np
from scipy.optimize import minimize

# Définition de la fonction de coût
def C(xy):
    x, y = xy
    return x**2 + y**2 - 3*x - 4*y + x*y

# Définition de la fonction de gradient (optionnelle mais recommandée)
def grad_C(xy):
    x, y = xy
    return np.array([2*x - 3 + y, 2*y - 4 + x])

# Point de départ pour l'algorithme
x0 = np.array([0, 0])

# Minimisation de la fonction de coût
res = minimize(C, x0, method="BFGS", jac=grad_C)

# Affichage des valeurs optimales de x et y
print("Valeurs optimales : x = {:.4f}, y = {:.4f}".format(res.x[0], res.x[1]))
print("Valeur minimale de la fonction de coût : {:.4f}".format(res.fun))