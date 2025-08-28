import networkx as nx

# Création du graphe orienté pondéré à partir des données de l'exercice
G_dijkstra = nx.DiGraph()
G_dijkstra.add_weighted_edges_from([
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'D', 3),
    ('C', 'B', 1), ('C', 'D', 5), ('C', 'E', 4),
    ('D', 'G', 2),
    ('E', 'G', 3)
])

# 1. Application de l'algorithme de Dijkstra
shortest_path = nx.dijkstra_path(G_dijkstra, source='A', target='G')

# 2. Données du chemin et de la distance minimale
path_length = nx.dijkstra_path_length(G_dijkstra, source='A', target='G')

print("--- Résultat de l'algorithme de Dijkstra ---")
print(f"Chemin le plus court de A à G : {shortest_path}")
print(f"Distance minimale : {path_length} km")