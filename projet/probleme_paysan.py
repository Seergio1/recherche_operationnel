from collections import deque

# Chaque état est un tuple : (paysan, loup, agneau, chou)
# G = Gauche, D = Droite
initial_state = ('G', 'G', 'G', 'G')
goal_state = ('D', 'D', 'D', 'D')

def est_valide(etat):
    p, l, a, c = etat
    # Si le paysan n'est pas là :
    if (p != l == a):  # le loup mange l'agneau
        return False
    if (p != a == c):  # l'agneau mange le chou
        return False
    return True

def deplacements_possibles(etat):
    p, l, a, c = etat
    opposé = 'D' if p == 'G' else 'G'
    actions = []

    # Le paysan se déplace seul
    nouvel_etat = (opposé, l, a, c)
    if est_valide(nouvel_etat):
        actions.append((nouvel_etat, "Paysan seul"))

    # Le paysan prend le loup
    if l == p:
        nouvel_etat = (opposé, opposé, a, c)
        if est_valide(nouvel_etat):
            actions.append((nouvel_etat, "Paysan + Loup"))

    # Le paysan prend l’agneau
    if a == p:
        nouvel_etat = (opposé, l, opposé, c)
        if est_valide(nouvel_etat):
            actions.append((nouvel_etat, "Paysan + Agneau"))

    # Le paysan prend le chou
    if c == p:
        nouvel_etat = (opposé, l, a, opposé)
        if est_valide(nouvel_etat):
            actions.append((nouvel_etat, "Paysan + Chou"))

    return actions

def recherche_solution():
    file = deque()
    file.append((initial_state, []))
    visites = set()

    while file:
        etat, chemin = file.popleft()

        if etat in visites:
            continue
        visites.add(etat)

        if etat == goal_state:
            return chemin + [(etat, "Fin")]

        for suivant, action in deplacements_possibles(etat):
            file.append((suivant, chemin + [(etat, action)]))

    return None

# Exécution
solution = recherche_solution()
if solution:
    for etat, action in solution:
        print(f"{etat} -> {action}")
else:
    print("Aucune solution trouvée.")
