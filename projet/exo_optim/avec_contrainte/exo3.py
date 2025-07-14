import numpy as np
from scipy.optimize import minimize

# Définition de la fonction à minimiser
def f(xy):
    x, y = xy
    return (x - 2)**2 + (y + 1)**2

# Définition de la contrainte d'égalité
def cons(xy):
    x, y = xy
    return x + 2*y - 3

# Définition des contraintes
con1 = {'type': 'eq', 'fun': cons}

# Point de départ pour l'algorithme
x0 = np.array([1, 1])

# Minimisation de la fonction sous contrainte
res = minimize(f, x0, method="SLSQP", constraints=con1)

# Affichage de la solution optimale
print("Solution optimale : x = {:.4f}, y = {:.4f}".format(res.x[0], res.x[1]))
print("Valeur minimale de la fonction : {:.4f}".format(res.fun))