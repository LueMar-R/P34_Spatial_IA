from tsp_graph_init import Graph, Route
import numpy as np
import random
import time
import pandas as pd
import time

random.seed(40)

class TSP_SA:

    def __init__(self, largeur, hauteur, nb_lieux):

        self.N = nb_lieux
        self.T0 = 1
        self.Tf = 0.01
        self.tau = 5000
        self.kmax = 100_000

        self.graphe = Graph(largeur, hauteur, nb_lieux)
        self.chemin_zero = self.heuristique()
        self.distance_zero = Route.calcul_distance_route(self.chemin_zero, self.graphe.matrice_od)
        # self.chemin_2opt = self.two_opt(self.chemin_zero)
        # self.distance_2opt = Route.calcul_distance_route(self.chemin_2opt, self.graphe.matrice_od)
        self.chemin_SA = self.recuit_simule()
        self.distance_SA = Route.calcul_distance_route(self.chemin_SA, self.graphe.matrice_od)      


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
        cheapest = Route.calcul_distance_route(best, self.graphe.matrice_od)
        better = True
        print("BEST", best, "- CHEAPEST", cheapest)
        print("Running 2opt")
        while better :
            better = False
            for i in range(1, len(trajet)-2) :
                for j in range(i+1, len(trajet)) :
                    if j-i == 1: 
                        continue
                    trajet2 = trajet[:]
                    trajet2[i:j] = trajet[j-1:i-1:-1]
                    #print("NEW ORDER TRY", trajet2)
                    #print("THIS COSTS", Route.calcul_distance_route(trajet2, self.graphe.matrice_od))
                    if Route.calcul_distance_route(trajet2, self.graphe.matrice_od) < cheapest:
                        best = trajet2
                        cheapest = Route.calcul_distance_route(best, self.graphe.matrice_od)
                        better = True
                        print("ACCEPTED")
                        print("NEW BEST ORDER :", trajet)
            trajet = best
        return best

    def perm_2opt(self, trajet):
        for i in range(1, len(trajet)-2) :
            for j in range(i+1, len(trajet)) :
                if j-i == 1: 
                    continue
                trajet2 = trajet[:]
                trajet2[i:j] = trajet[j-1:i-1:-1]
                if Route.calcul_distance_route(trajet2, self.graphe.matrice_od) < Route.calcul_distance_route(trajet, self.graphe.matrice_od):
                    best = trajet2
        return best


    def permutation(self, i, j, trajet):
        self.route = trajet
        mini = min(i,j)
        maxi = max(i,j)
        self.route[mini:maxi] = self.route[mini:maxi].copy()[::-1]
        return self.route

    def recuit_simule(self):
        #initialisation des variables
        T = self.T0
        trajet1 = self.chemin_zero.copy()
        cost1 = self.distance_zero
        best = self.chemin_zero.copy()
        cheapest = self.distance_zero

        print("BEST", trajet1)
        print("CHEAPEST", cost1)
        k=0
        while T>self.Tf and k<self.kmax:
            # i = random.randint(1,self.N)
            # j = random.randint(1,self.N)
            # if j-i == 1: 
            #     continue
            trajet2 = self.two_opt(trajet1)
            cost2 = Route.calcul_distance_route(trajet2, self.graphe.matrice_od)
            print("NEW ORDER TRY", trajet2)
            print("    THIS COSTS", cost2)
            if cost2 < cheapest:
                best = trajet1 = trajet2
                cheapest = cost1 = cost2
                print("    ACCEPTED +  BEST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else :
                if cost2 < cost1:
                    trajet1 = trajet2
                    cost1 = cost2
                else :
                    a = np.random.uniform()
                    if a > np.exp(-0.5*T):
                        trajet1 = trajet2
                        cost1 = cost2
                        print("    ACCEPTED", a, ">" , np.exp(-0.5*T))
                    else :
                        print("    REJECTED", a, "<" , np.exp(-0.5*T))
            k+=1
            T = T*np.exp(-T/self.tau)
            print("    >> tempetature :", T)
            print("trajet1", trajet1)
            print("trajet2", trajet2)
            print("best   ", best)
            print(k, "k")
            print("- "*50)
        return best




def test(l, h, np):
    a=time.time()
    algo = TSP_SA(l, h, np)
    
    print("**route de départ**\t", algo.chemin_zero)
    print("**distance zéro**", algo.distance_zero)
    # print("**route 2opt**\t\t", algo.chemin_2opt)
    # print("**distance 2opt**", algo.distance_2opt)
    print("**route SA**\t\t", algo.chemin_SA)
    print("**distance SA**", algo.distance_SA)
    print("**temps de calcul (s)**", time.time()-a)

test(600,800,50)
