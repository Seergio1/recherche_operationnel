import networkx as nx
# Ford Fulkerson
# Création du graphe orienté avec les capacités des conduites
G_flow = nx.DiGraph()
G_flow.add_edge('S', 'A', capacity=10)
G_flow.add_edge('S', 'B', capacity=5)
G_flow.add_edge('A', 'B', capacity=15)
G_flow.add_edge('A', 'T', capacity=5)
G_flow.add_edge('B', 'T', capacity=10)

# 1. Calcul du flot maximal
max_flow_value, flow_dict = nx.maximum_flow(G_flow, 'S', 'T')

# 2. Affichage de la répartition des flots
print("--- Résultat du Flot Maximal (Ford-Fulkerson) ---")
print(f"Flot maximal entre S et T : {max_flow_value}\n")
print("Répartition des flots sur les arcs :")
for u, v_flows in flow_dict.items():
    for v, flow_value in v_flows.items():
        if flow_value > 0:
            print(f"  - Flot sur l'arc ({u}, {v}) : {flow_value}")

# Vérification du flot total (somme des flots sortant de S)
flot_total_sortant_de_S = sum(flow_dict['S'].values())
print(f"\nLe flot total sortant de la source S est de {flot_total_sortant_de_S}.")