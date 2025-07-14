import numpy as np
from scipy.optimize import minimize

# Définition de la fonction à minimiser
def f(xy):
    x, y = xy
    return (x - 1)**2 + (y - 2)**2 + x*y

# Définition de la fonction de gradient (optionnelle mais recommandée pour BFGS)
# def grad_f(xy):
#     x, y = xy
#     return np.array([2*(x - 1) + y, 2*(y - 2) + x])

# Point de départ pour l'algorithme
x0 = np.array([0, 0])

# Minimisation de la fonction
res = minimize(f, x0, method="BFGS")
# res = minimize(f, x0, method="BFGS", jac=grad_f)

# Affichage de la solution optimale
print("Solution optimale : x = {:.4f}, y = {:.4f}".format(res.x[0], res.x[1]))
print("Valeur minimale de la fonction : {:.4f}".format(res.fun))