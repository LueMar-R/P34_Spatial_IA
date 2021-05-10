import numpy as np
import random
import time
import pandas as pd

"""pour appeler la fonction "generer" via l'invite de commande : 
    $ python tsp_graph_init.py name l w np

    Args:
        name (str): nom du fichier csv qui sera généré
        l (int): largeur de l'espace 
        h (int): hauteur de l'espace
        np (int): nombre de points
"""

class Lieu:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def distance(cls, lieu1, lieu2):
        return np.sqrt((lieu1.x-lieu2.x)**2 + (lieu1.y-lieu2.y)**2)


class Graph:

    def __init__(self, largeur, hauteur, nb_lieux):
        self.LARGEUR = largeur
        self.HAUTEUR = hauteur
        self.NB_LIEUX = nb_lieux
        self.liste_lieux = self.creer_liste_lieux()
        self.matrice_od = self.calcul_matrice_cout_od()
        self.ordre = Route.def_ordre(self.NB_LIEUX)
        self.distance = self.calcul_distance_route()

    def creer_liste_lieux(self):
        self.liste_lieux=[]
        for i in range(self.NB_LIEUX):
            x = random.uniform(0, self.LARGEUR)
            y = random.uniform(0, self.HAUTEUR)
            point = Lieu(x,y)
            self.liste_lieux.append(point)
        return self.liste_lieux

    def calcul_matrice_cout_od(self):
        self.matrice_od = np.zeros((self.NB_LIEUX, self.NB_LIEUX))
        for i in range(self.NB_LIEUX):
            for j in range(self.NB_LIEUX):
                if i == j:
                    self.matrice_od[i,j] = np.inf
                if i != j:
                    self.matrice_od[i,j] = Lieu.distance(self.liste_lieux[i], self.liste_lieux[j])
        return self.matrice_od
    
    def calcul_distance_route(self) :
        self.distance = 0
        for i in range(len(self.ordre)-1):
            self.distance += self.matrice_od[self.ordre[i],self.ordre[i+1]]
        return self.distance
    
    @classmethod
    def plus_proche_voisin(cls, lieu, matrice_od) :
        cls.le_plus_proche_voisin = np.argmin(matrice_od[lieu])
        return cls.le_plus_proche_voisin

    def sauvegarder_graph(self, path):
        self.df = pd.DataFrame([(lieu.x, lieu.y) for lieu in self.liste_lieux], columns =['x','y'])
        self.df.to_csv(path, index=False)
    
    @classmethod
    def charger_graph(cls, path):
        return pd.read_csv(path).values


class Route:
    
    @classmethod
    def def_ordre(cls, nb_lieux):
        cls.ordre = [0]
        tmp = list(range(1,nb_lieux))
        random.shuffle(tmp)
        cls.ordre.extend(tmp)
        cls.ordre.append(0)
        return cls.ordre


class TSP_SA:

    def __init__(self, largeur, hauteur, nb_lieux):
        self.graphe = Graph(largeur, hauteur, nb_lieux)
        self.chemin_zero = self.heuristique()


    def heuristique(self):
        print("HEURISTIQUE")
        local_matrix = self.graphe.matrice_od
        local_places_list = self.graphe.liste_lieux
        route_naive = [local_places_list[0]]
        for i in range(self.graphe.NB_LIEUX):
            print(route_naive)
            last_point = local_places_list.index(route_naive[-1])
            print(">>", last_point)
            plus_proche = self.graphe.plus_proche_voisin(last_point, local_matrix)
            print(local_matrix)
            local_matrix = np.delete(local_matrix, plus_proche, 0)
            local_matrix = np.delete(local_matrix, plus_proche, 1)
            route_naive.append(local_places_list[plus_proche])
            print(local_matrix)
            local_places_list.pop(last_point)
            print([(lieu.x, lieu.y) for lieu in route_naive])
        return route_naive






def generer(name, l, h, np):

    graphe = Graph(l, h, np)

    print("liste des lieux à visiter :")
    print([(lieu.x, lieu.y) for lieu in graphe.liste_lieux])
    print("matrice des distances :")
    print(graphe.matrice_od)

    print("*"*65)

    print("nombre de lieux :", graphe.NB_LIEUX, "__ ordre de visite :", graphe.ordre)

    print("distance totale :", graphe.distance)

    graphe.sauvegarder_graph(f"{name}.csv")

def test(l, h, np):
    algo = TSP_SA(l, h, np)
    
    print("**route de départ**", algo.chemin_zero)


test(10,10,5)
#generer("points", 10, 10, 5)

# if __name__ == "__main__":
#     import sys
#     generer(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))





## permutations dans une route : voir algo 2opt