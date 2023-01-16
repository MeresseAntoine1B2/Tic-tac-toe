plateau = {
    "A" : [None for _ in range(3)],
    "B" : [None for _ in range(3)],
    "C" : [None for _ in range(3)]
}

def afficher_grille(plateau:dict) -> None:
    """Fonction qui affiche la grille du morpion

    Args:
        plateau (dict): Un plateau de jeu
    """
    print(" \t|\t0\t|\t1\t|\t2\t|")
    print("---------------------------------------------------------")
    for cle in plateau:
        print(cle, end="\t|\t")
        for elt in plateau[cle]:
            if elt == None:
                print(" ", end="\t|\t")
            else:
                print(elt, end="\t|\t")
        print("\n---------------------------------------------------------")

def jouer_coup(plateau:dict, joueur:str, coup:str) -> None:
    """Fonction qui joue un coup (Ne vérifie pas si le coup est valide)

    Args:
        plateau (dict): Le plateau de jeu
        joueur (str): "O" ou "X"
        coup (str): Coordonnées de la forme "A1"
    """
    plateau[coup[0]][int(coup[1])] = joueur
    
