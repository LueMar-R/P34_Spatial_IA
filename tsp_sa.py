from tsp_graph_init import Graph, Route
import numpy as np
import random


random.seed(1)
np.random.seed(1)

class TSP_SA:

    def __init__(self, largeur, hauteur, liste_lieux=False, nb_lieux=25):

        self.graphe = Graph(largeur, hauteur, liste_lieux, nb_lieux)
        self.chemin_zero = self.heuristique()
        self.N = len(self.chemin_zero)-1

        self.distance_zero = Route.calcul_distance_route(self.chemin_zero, self.graphe.matrice_od)
 
        self.T0 = 0.50
        self.Tf = 0.25
        self.tau = 500
        self.kmax = min(self.N*10, 4_000)

    def heuristique(self):
        local_matrix = self.graphe.matrice_od.copy()
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
        trajet1 = trajet.copy()
        cheapest = Route.calcul_distance_route(best, self.graphe.matrice_od)
        better = True
        while better :
            better = False
            for i in range(1, len(trajet1)-2) :
                for j in range(i+1, len(trajet1)) :
                    if j-i == 1: 
                        continue
                    trajet2 = trajet1[:]
                    trajet2[i:j] = trajet1[j-1:i-1:-1]
                    if Route.calcul_distance_route(trajet2, self.graphe.matrice_od) < cheapest:
                        best = trajet2
                        cheapest = Route.calcul_distance_route(best, self.graphe.matrice_od)
                        better = True
            trajet1 = best
            yield best, trajet2, cheapest
        return best

    def SA_two_opt(self, trajet): ## Moins bon, non utilisé pour la démonstration
        best = trajet.copy()
        trajet1 = trajet.copy()
        cheapest = Route.calcul_distance_route(best, self.graphe.matrice_od)
        print("BEST", best, "- CHEAPEST", cheapest)
        T = self.T0
        k=0
        q=0
        while T>self.Tf and k<self.kmax:
            for i in range(1, len(trajet1)-2) :
                for j in range(i+1, len(trajet1)) :
                    if j-i == 1: 
                        continue
                    trajet2 = trajet1[:]
                    trajet2[i:j] = trajet1[j-1:i-1:-1]
                    cost2 = Route.calcul_distance_route(trajet2, self.graphe.matrice_od)
                    if cost2 < cheapest:
                        best = trajet1 = trajet2
                        cheapest = cost1 = cost2
                        print("NEW BEST ORDER n°", q)
                        print("THIS COSTS", cost2)
                        q+=1
                    else :
                        a = np.random.uniform()
                        if a > np.exp(-0.5*T):
                            trajet1 = trajet2[:]
                yield best, trajet2, cheapest
            k+=1
            T = T*np.exp(-T/self.tau)           
            trajet1 = best
            print(k, "k", np.round(T,2), "°     THIS COSTS", cost2)
        return best
