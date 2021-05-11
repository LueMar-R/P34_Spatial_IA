import Lieu
import numpy
import pandas
import random


class Graph:
    """Cette classe est utilisée pour mémoriser une liste de lieux"""
    matrice_od = pandas.DataFrame(columns=['LieuA', 'LieuB', 'Distance'])

    def __init__(self, nb_l, l, h):
        self.LARGEUR = l
        self.HAUTEUR = h
        self.NB_LIEUX = nb_l
        self.liste_lieux = numpy.empty((0, nb_l))

        for i in range(0, nb_l - 1):
            self.liste_lieux[i] = Lieu.Lieu(random.randint(0, l), random.randint(0, h))

    def __repr__(self):
        return "<Graph : nombre de lieu = {}, largeur = {}, hauteur = {}>".format(self.NB_LIEUX, self.LARGEUR, self.HAUTEUR)

    def __str__(self):
        return "Nombre de lieu = {}, Largeur = {}, Hauteur = {}\n{}".format(self.NB_LIEUX, self.LARGEUR, self.HAUTEUR, self.liste_lieux)
    
    def calcul_matrice_cout_od(self):
        """calculer une matrice de distances entre chaque lieu du graphe"""
        for i in self.liste_lieux:
            for j in self.liste_lieux:
                Graph.matrice_od.append({'LieuA' : i, 'LieuB' : j, 'Distance' : i.distance(j) })

    def plus_proche_voisin(self, L, reste = Graph.matrice_od):
        """renvoyer le plus proche voisin d'un lieu"""
        voisins = reste[reste['LieuA'] != L]
        ligne_proche = voisins[voisins['Distance'] == voisins['Distance'].min()]
        return ligne_proche['LieuB']
    
    def charger_graph(self, fichier):
        df = pandas.read_csv(fichier)
        return df.values

    def sauvegarder_graph(self, fichier):
        df = pandas.DataFrame(self.liste_lieux)
        df.to_csv(fichier)

if __name__ == "__main__":
    from matplotlib import pyplot as plt

    lt = 20
    ht = 20
    nb = 5

    gt = Graph(nb, lt, ht)

    print(gt)

    

    pt1 = Lieu(xt1, yt1)

    print("{}".format(pt1))

    plt.plot(pt1.x, pt1.y, marker="o", color="blue")
    plt.show()