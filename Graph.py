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
        l_lieux = []

        for i in range(nb_l):
            n = Lieu.Lieu(random.randint(0, l), random.randint(0, h))
            while n in l_lieux:
                n = Lieu.Lieu(random.randint(0, l), random.randint(0, h))
            l_lieux.append(n)
        self.liste_lieux = numpy.array(l_lieux)

    def __repr__(self):
        return "<Graph : nombre de lieu = {}, largeur = {}, hauteur = {}>".format(self.NB_LIEUX, self.LARGEUR, self.HAUTEUR)

    def __str__(self):
        return "Graph : Nombre de lieu = {}, Largeur = {}, Hauteur = {}\n{}".format(self.NB_LIEUX, self.LARGEUR, self.HAUTEUR, self.liste_lieux)
    
    def calcul_matrice_cout_od(self):
        """calculer une matrice de distances entre chaque lieu du graphe"""
        for i in self.liste_lieux:
            for j in self.liste_lieux:
                if(i != j) :
                    Graph.matrice_od = Graph.matrice_od.append({'LieuA' : i, 'LieuB' : j, 'Distance' : i.distance(j) }, ignore_index=True)

    def plus_proche_voisin(self, L, reste):
        """renvoyer le plus proche voisin d'un lieu"""
        # print("fonction plus_proche_voisin")
        # print("L ={}".format(L))
        # print("reste =\n{}".format(reste))
        voisins = reste[reste['LieuA'] == L]
        # print("voisins =\n{}".format(voisins))
        ligne_proche = voisins[voisins['Distance'] == voisins['Distance'].min()]
        # print("ligne_proche =\n{}".format(ligne_proche))
        return ligne_proche.iat[0, 1]
    
    def charger_graph(self, fichier):
        df = pandas.read_csv(fichier)
        return df.values

    def sauvegarder_graph(self, fichier):
        df = pandas.DataFrame(self.liste_lieux)
        df.to_csv(fichier)

if __name__ == "__main__":
    lt = 20
    ht = 20
    nb = 5
    gt = Graph(nb, lt, ht)

    print("graph =\n{}\n".format(gt))


    gt.calcul_matrice_cout_od()

    print("Matrice =\n{}\n".format(Graph.matrice_od))
    

    pt1 = Graph.matrice_od.iat[0, 0]
    pt2 = gt.plus_proche_voisin(pt1, Graph.matrice_od)
    print("Le lieu le plus proche de {} est {}\n".format(pt1, pt2))