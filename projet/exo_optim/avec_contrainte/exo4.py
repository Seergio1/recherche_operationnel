import numpy as np
from scipy.optimize import minimize

# Définition de la fonction à minimiser
def L(xy):
    x, y = xy
    return 3*x**2 + 2*y**2 + x*y

# Définition de la contrainte
def cons(xy):
    x, y = xy
    return x + y - 100

# Définition des contraintes
con1 = {'type': 'eq', 'fun': cons}

# Point de départ pour l'algorithme
x0 = np.array([50, 50])

# Minimisation de la fonction sous contrainte
res = minimize(L, x0, method="SLSQP", constraints=con1)

# Affichage de la solution optimale
print("Solution optimale : x = {:.4f}, y = {:.4f}".format(res.x[0], res.x[1]))
print("Valeur minimale de la fonction : {:.4f}".format(res.fun))