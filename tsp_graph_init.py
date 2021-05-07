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

    @classmethod
    def creer_liste_lieux(cls):
        cls.LARGEUR = 6
        cls.HAUTEUR = 10
        cls.NB_LIEUX = 4
        cls.liste_lieux = []
        for i in range(cls.NB_LIEUX):
            x = random.uniform(0, cls.LARGEUR)
            y = random.uniform(0, cls.HAUTEUR)
            cls.liste_lieux.append([x,y])
        return cls.liste_lieux

    @classmethod
    def calcul_matrice_cout_od(cls, liste_lieux):
        cls.LEN = len(liste_lieux)
        cls.matrice_od = np.zeros((cls.LEN, cls.LEN))
        for i in range(cls.LEN):
            for j in range(cls.LEN):
                if i == j:
                    cls.matrice_od[i,j] = np.inf
                if i != j:
                    cls.matrice_od[i,j] = Lieu.distance(liste_lieux[i], liste_lieux[j])
        return cls.matrice_od
        
    @classmethod    
    def plus_proche_voisin(cls, lieu, matrice_od) :
        cls.le_plus_proche_voisin = np.argmin(matrice_od[lieu])
        return cls.le_plus_proche_voisin

    @classmethod
    def sauvegarder_graph(cls, liste_lieux, path):
        cls.df = pd.DataFrame(liste_lieux, columns =['x','y'])
        cls.df.to_csv(path, index=False)
    
    @classmethod
    def charger_graph(cls, path):
        cls.path = path
        return pd.read_csv(cls.path)


class Route:
    def __init__(self):
        pass

class Affichage:
    pass


l_lieux = Graph.creer_liste_lieux()
print(l_lieux)

matrice_cout = Graph.calcul_matrice_cout_od(l_lieux)
print(matrice_cout)

voisin_1 = Graph.plus_proche_voisin(1, matrice_cout)
voisin_2 = Graph.plus_proche_voisin(2, matrice_cout)
print(voisin_1)
print(voisin_2)

Graph.sauvegarder_graph(l_lieux, "data.csv")

df = Graph.charger_graph("data.csv")
print(df)

