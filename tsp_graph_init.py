import numpy as np
import random
import time
import pandas as pd

class Lieu:
    @classmethod
    def def_lieu(cls, x, y):
        return (float(x), float(y))

    @classmethod
    def distance(cls, lieu1, lieu2):
        return np.sqrt((lieu1[0]-lieu2[0])**2 + (lieu1[1]-lieu2[1])**2)


class Graph:

    def __init__(self, largeur=10, hauteur=10, nb_lieux=5):
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
            self.liste_lieux.append([x,y])
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
        self.df = pd.DataFrame(self.liste_lieux, columns =['x','y'])
        self.df.to_csv(path, index=False)
    
    @classmethod
    def charger_graph(cls, path):
        return pd.read_csv(path).values


class Route:
    
    @classmethod
    def def_ordre(cls, nb_lieux):
        cls.ordre = [0]
        tmp = [i for i in range(1,nb_lieux)]
        random.shuffle(tmp)
        cls.ordre.extend(tmp)
        cls.ordre.append(0)
        return cls.ordre


def main():

    graphe = Graph(12, 12, 8)

    print("liste des lieux à visiter :")
    print(graphe.liste_lieux)
    print("matrice des distances :")
    print(graphe.matrice_od)

    print("*"*73)

    print("nombre de lieux :", graphe.NB_LIEUX, "ordre de visite :", graphe.ordre)

    print("distance totale :", graphe.distance)

    graphe.sauvegarder_graph("points.csv")

main()