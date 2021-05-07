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

    def __init__(self, largeur, hauteur, nb_lieux):
        self.LARGEUR = largeur
        self.HAUTEUR = hauteur
        self.NB_LIEUX = nb_lieux
        self.liste_lieux = self.creer_liste_lieux()
        self.matrice_od = self.calcul_matrice_cout_od

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
        return pd.read_csv(path).values

    @classmethod
    def calcul_distance_route(cls, matrice_od, route) :
        cls.longueur = 0
        for i in range(len(route)-1):
            cls.longueur += matrice_od[route[i],route[i+1]]
        return cls.longueur


class Route:

    @classmethod
    def def_ordre(cls, NB_LIEUX):
        cls.ordre = [0]
        tmp = [i for i in range(1,NB_LIEUX)]
        random.shuffle(tmp)
        cls.ordre.extend(tmp)
        cls.ordre.append(0)
        return cls.ordre
        

class Affichage:
    pass




tutu = Graph(6, 10, 4)

matrice_cout = tutu.calcul_matrice_cout_od()
print(matrice_cout)

voisin_1 = tutu.plus_proche_voisin(1, matrice_cout)
voisin_2 = tutu.plus_proche_voisin(2, matrice_cout)
print(voisin_1)
print(voisin_2)

route = Route.def_ordre(len(matrice_cout))
print(route)

longueur = tutu.calcul_distance_route(matrice_cout, route)
print(longueur)