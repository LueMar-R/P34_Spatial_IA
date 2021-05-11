from tsp_graph_init import Graph, Route
import numpy as np
import random
import time
import pandas as pd
from itertools import permutations

class TSP_SA:

    def __init__(self, largeur, hauteur, nb_lieux):
        self.graphe = Graph(largeur, hauteur, nb_lieux)
        self.chemin_zero = self.heuristique()
        self.distance_zero = Route.calcul_distance_route(self.chemin_zero, self.graphe.matrice_od)
        self.chemin_2opt = self.two_opt(self.chemin_zero)
        self.distance_2opt = Route.calcul_distance_route(self.chemin_2opt, self.graphe.matrice_od)


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

    def two_opt(self, trajet):
        best = trajet.copy()
        cheapest = self.distance_zero
        better = True
        print("BEST", best)
        print("CHEAPEST", cheapest)
        while better :
            better = False
            for i in range(1, len(trajet)-2) :
                for j in range(i+1, len(trajet)) :
                    if j-i == 1: 
                        continue
                    trajet2 = trajet[:]
                    trajet2[i:j] = trajet[j-1:i-1:-1]
                    print("NEW ORDER TRY", trajet2)
                    print("THIS COSTS", Route.calcul_distance_route(trajet2, self.graphe.matrice_od))
                    if Route.calcul_distance_route(trajet2, self.graphe.matrice_od) < cheapest:
                        best = trajet2
                        cheapest = Route.calcul_distance_route(best, self.graphe.matrice_od)
                        better = True
                        print("ACCEPTED")
                    else :
                        print("REJECTED")

            trajet = best
            print("NEW BEST ORDER :", trajet)
        return best



    
    # def recuit_simule(self):
    #     #constantes
    #     N = self.graphe.NB_LIEUX
    #     T0 = 10.0
    #     Tf = 0.01
    #     tau = 0.0001

    #     #initialisation des variables
    #     trajet = self.chemin_zero.copy()
    #     distance = self.distance_zero




def test(l, h, np):
    algo = TSP_SA(l, h, np)
    
    print("**route de départ**\t", algo.chemin_zero)
    print("**distance zéro**", algo.distance_zero)
    print("**route 2opt**\t\t", algo.chemin_2opt)
    print("**distance 2opt**", algo.distance_2opt)


test(100,100,12)