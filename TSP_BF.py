from itertools import combinations


class TSP_BF:
    """Classe permettant de résoudre itérativement le problème du plus court circuit visitant tous les lieux et retournant au point de départ en utilisant un algorithme brute force."""

    def __init__(self, g, i) -> None:
        c = '#000000'
        for i in combinations(g.liste_lieux + [g.liste_lieux[0]], len(g.liste_lieux)+2):
            