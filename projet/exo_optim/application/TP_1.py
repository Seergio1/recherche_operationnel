from pulp import LpMaximize, LpProblem, LpVariable, LpBinary

# Données corrigées du TP 1
# objets = ["1", "2", "3"]
# valeurs = {"1": 20, "2": 15,"3": 10}
# poids = {"1": 5, "2": 3,"3": 2}
objets = ["A", "B", "C", "D"]
valeurs = {"A": 40, "B": 30, "C": 20, "D": 10}
poids = {"A": 6, "B": 4, "C": 3, "D": 2}
capacite_max = 10

# Création du modèle
modele_sac = LpProblem(name="sac-a-dos", sense=LpMaximize)

# Variables de décision
x = LpVariable.dicts("Choix_objet", objets, cat=LpBinary)

# Fonction objectif
modele_sac += sum(valeurs[i] * x[i] for i in objets), "Valeur_maximale"

# Contrainte de poids
modele_sac += sum(poids[i] * x[i] for i in objets) <= capacite_max, "Poids_maximal"

# Résolution
modele_sac.solve()

# Affichage des résultats
print("--- TP 1 : Problème du Sac à Dos ---")
print(f"Statut de la solution : {modele_sac.status}")
print(f"Valeur maximale : {modele_sac.objective.value():.2f}")
print("Objets choisis :")
for objet in objets:
    if x[objet].value() == 1:
        print(f"  - L'objet {objet} est choisi.")
print("\n" + "-"*40 + "\n")