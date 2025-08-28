from pulp import LpMinimize, LpProblem, LpVariable, LpBinary

# 1. Définir les données du problème (tirées de Tp_Programme_Lineaire.pdf)
ouvriers = ["O1", "O2", "O3"]
taches = ["T1", "T2", "T3"]

# Matrice des coûts (coût_ouvrier_tache)
# couts = {
#     ("O1", "T1"): 2, ("O1", "T2"): 4, ("O1", "T3"): 3,
#     ("O2", "T1"): 3, ("O2", "T2"): 2, ("O2", "T3"): 5,
#     ("O3", "T1"): 4, ("O3", "T2"): 3, ("O3", "T3"): 2
# }
couts = {
    ("O1", "T1"): 6, ("O1", "T2"): 4, ("O1", "T3"): 3,
    ("O2", "T1"): 2, ("O2", "T2"): 6, ("O2", "T3"): 5,
    ("O3", "T1"): 4, ("O3", "T2"): 3, ("O3", "T3"): 7
}

# 2. Créer le modèle d'optimisation (minimisation)
modele_affectation = LpProblem(name="affectation-ouvrier-tache", sense=LpMinimize)

# 3. Définir les variables de décision (binaires)
x = LpVariable.dicts("Affectation", ((o, t) for o in ouvriers for t in taches), cat=LpBinary)

# 4. Définir la fonction objectif (minimiser le coût total)
modele_affectation += sum(couts[(o, t)] * x[(o, t)] for o in ouvriers for t in taches), "Cout_total"

# 5. Ajouter les contraintes
# Chaque ouvrier est affecté à une seule tâche
for o in ouvriers:
    modele_affectation += sum(x[(o, t)] for t in taches) == 1, f"Affectation_ouvrier_{o}"

# Chaque tâche est affectée à un seul ouvrier
for t in taches:
    modele_affectation += sum(x[(o, t)] for o in ouvriers) == 1, f"Affectation_tache_{t}"

# 6. Résoudre le problème
modele_affectation.solve()

# 7. Afficher les résultats
print("--- Solution du Problème d'Affectation ---")
print(f"Statut de la solution : {modele_affectation.status}")
print(f"Coût total minimal : {modele_affectation.objective.value():.2f} €")
print("Affectations optimales :")
for o in ouvriers:
    for t in taches:
        if x[(o, t)].value() == 1:
            print(f"  - L'ouvrier {o} est affecté à la tâche {t}.")