from pulp import *

# 1. Définir les données du problème
# villes = ["A", "B", "C", "D"]
# distances = {
#     ("A", "B"): 10, ("A", "C"): 15, ("A", "D"): 20,
#     ("B", "A"): 10, ("B", "C"): 35, ("B", "D"): 25,
#     ("C", "A"): 15, ("C", "B"): 35, ("C", "D"): 30,
#     ("D", "A"): 20, ("D", "B"): 25, ("D", "C"): 30
# }
villes = ["A", "B", "C", "D","E"]
distances = {
    ("A", "B"): 12, ("A", "C"): 10, ("A", "D"): 19, ("A", "E"): 8,
    ("B", "A"): 12, ("B", "C"): 3, ("B", "D"): 7, ("B", "E"): 6,
    ("C", "A"): 10, ("C", "B"): 3, ("C", "D"): 2, ("C", "E"): 4,
    ("D", "A"): 19, ("D", "B"): 7, ("D", "C"): 2, ("D", "E"): 3,
    ("E", "A"): 8, ("E", "B"): 6, ("E", "C"): 4, ("E", "D"): 3
}
arcs = distances.keys()

# 2. Créer le modèle
modele_tsp = LpProblem("Probleme_du_voyageur_de_commerce", LpMinimize)

# 3. Définir les variables de décision
x = LpVariable.dicts("Route", arcs, cat=LpBinary)
u = LpVariable.dicts("SousTour", villes, lowBound=1, upBound=len(villes), cat=LpInteger)

# 4. Fonction objectif
modele_tsp += lpSum(distances[i, j] * x[i, j] for i, j in arcs)

# 5. Ajouter les contraintes
# Chaque ville a exactement une route entrante et une sortante
for j in villes:
    modele_tsp += lpSum(x[i, j] for i in villes if i != j) == 1
for i in villes:
    modele_tsp += lpSum(x[i, j] for j in villes if i != j) == 1

# Contraintes d'élimination des sous-tours
n = len(villes)
for i in villes:
    for j in villes:
        if i != j and i != "A" and j != "A": 
            modele_tsp += u[i] - u[j] + n * x[i, j] <= n - 1

# 6. Résoudre le problème
modele_tsp.solve()

# 7. Afficher les résultats
print("--- Solution du Problème du Voyageur de Commerce (TSP) ---")
print(f"Statut de la solution : {modele_tsp.status}")
print(f"Distance minimale du circuit : {modele_tsp.objective.value():.2f}")
print("Chemin optimal :")
depart = "A"
chemin_final = [depart]
while True:
    prochaine_ville = next(j for i, j in arcs if x[i, j].value() == 1 and i == depart)
    chemin_final.append(prochaine_ville)
    depart = prochaine_ville
    if depart == "A":
        break
print(" -> ".join(chemin_final))