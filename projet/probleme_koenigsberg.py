# Créer le graphe non orienté
# import matplotlib.pyplot as plt
# import networkx as nx

# G = nx.MultiGraph()

# # Sommets
# G.add_nodes_from(["A", "B", "C", "D"])

# # Arêtes
# G.add_edge("A", "B")
# G.add_edge("A", "B")
# G.add_edge("A", "C")
# G.add_edge("A", "C")
# G.add_edge("B", "D")
# G.add_edge("C", "D")
# G.add_edge("A", "D")

# # Degrés
# print("Degrés des sommets :")
# for node in G.nodes:
#     print(f"{node} : {G.degree(node)}")

# # Vérification eulérienne
# impairs = [n for n in G.nodes if G.degree(n) % 2 == 1]
# if len(impairs) == 0:
#     print("✅ Cycle eulérien possible")
# elif len(impairs) == 2:
#     print("✅ Chemin eulérien possible")
# else:
#     print("❌ Aucun chemin ni cycle eulérien possible")

# # Affichage
# pos = nx.spring_layout(G, seed=42)
# nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=1000)
# nx.draw_networkx_labels(G, pos, font_size=14)

# # Afficher chaque arête multiple
# for (u, v, key) in G.edges(keys=True):
#     nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], connectionstyle=f'arc3, rad={0.1 * key}', edge_color='black')

# plt.title("Ponts de Königsberg")
# plt.axis("off")
# plt.show()





# Graphe des ponts de Königsberg verion simplifiée
def a_chemin_eulerien(graphe):
    impair = 0
    for sommet in graphe:
        if len(graphe[sommet]) % 2 != 0:
            impair += 1
    return impair == 0 or impair == 2


# ici c'est possible
# graphe = { 
#     'A': ['B', 'B', 'C'],
#     'B': ['A', 'A', 'C', 'C', 'D'],
#     'C': ['A', 'B', 'B', 'D'],
#     'D': ['B', 'C']
# }

#ici , ce n'est pas possible
graphe = {
    'A': ['B', 'B', 'C','C','D'],
    'B': ['A', 'A' , 'D'],
    'C': ['A', 'A' , 'D'],
    'D': ['B', 'C', 'A']
}

print("Chemin eulérien possible ?" , a_chemin_eulerien(graphe))  # Résultat : False
