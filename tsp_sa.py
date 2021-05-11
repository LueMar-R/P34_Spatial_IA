from tsp_graph_init import Graph, Route
import numpy as np
import random
import time
import pandas as pd

class TSP_SA:

    def __init__(self, largeur, hauteur, nb_lieux):
        self.graphe = Graph(largeur, hauteur, nb_lieux)
        self.chemin_zero = self.heuristique()
        self.distance_zero = Route.calcul_distance_route(self.chemin_zero, self.graphe.matrice_od)




    def heuristique(self):

        local_matrix = self.graphe.matrice_od.copy()
        local_places_list = self.graphe.liste_lieux
        points_a_explorer = list(range(1,self.graphe.NB_LIEUX))
        route_courte = [0]
        while points_a_explorer:
            last_point = route_courte[-1]
            plus_proche = self.graphe.plus_proche_voisin(last_point, local_matrix)
            local_matrix[:,last_point]= np.inf
            route_courte.append(plus_proche)
            points_a_explorer.remove(plus_proche)
        route_courte.append(0)

        return route_courte



def test(l, h, np):
    algo = TSP_SA(l, h, np)
    
    print("**route de départ**", algo.chemin_zero)
    print("**distance zéro**", algo.distance_zero)


test(10,10,5)