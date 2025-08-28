import networkx as nx

# 1. Modélisation du problème en graphe
# Les sommets sont les matières, les arêtes sont les conflits d'horaire.
matieres = ["Mathématiques", "Physique", "Chimie", "SVT", "Informatique"]
conflits = [("Mathématiques", "Physique"),
            ("Physique", "Chimie"),
            ("Chimie", "SVT"),
            ("SVT", "Informatique"),
            ("Informatique", "Mathématiques")]

# Créer un graphe non orienté
G = nx.Graph()
G.add_nodes_from(matieres)
G.add_edges_from(conflits)

# 2. Trouver le nombre chromatique et la coloration
# On utilise un algorithme glouton (heuristique) pour trouver une coloration valide.
# Le nombre de couleurs utilisées sera le nombre chromatique.
coloring = nx.coloring.greedy_color(G, strategy="largest_first")
num_colors = len(set(coloring.values()))

# 3. Proposer un emploi du temps compatible
print("--- Emploi du temps des examens ---")
print(f"Nombre de créneaux nécessaires (nombre chromatique): {num_colors}\n")

creneaux = {}
for matiere, couleur in coloring.items():
    if couleur not in creneaux:
        creneaux[couleur] = []
    creneaux[couleur].append(matiere)

for couleur, matieres_list in creneaux.items():
    print(f"Créneau horaire {couleur}:")
    for matiere in matieres_list:
        print(f"  - {matiere}")
print("\n----------------------------------")

# Note: La coloration gloutonne n'est pas toujours la plus optimale.
# Le graphe modélisé est un cycle de 5 sommets, dont le nombre chromatique est 3.
# L'algorithme glouton donnera donc une solution en 3 couleurs, qui est l'optimum.
# Créneau 0: Mathématiques, SVT
# Créneau 1: Physique, Informatique
# Créneau 2: Chimie