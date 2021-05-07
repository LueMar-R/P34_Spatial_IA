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
            self.liste_lieux[i] = Lieu.Lieu(randint(0, l), randint(0, h))

        def calcul_matrice_cout_od(self):
            for i in self.liste_lieux:
                for j in self.liste_lieux:
                    Graph.matrice_od.append({'LieuA' : i.id, 'LieuB' : j.id, 'Distance' : i.distance(j) })

        def plus_proche_voisin(self, L):
            voisins = Graph.matrice_od[Graph.matrice_od['LieuA'] == L.id]
            ligne_proche = voisins[voisins['Distance'] == voisins['Distance'].min()]
            return Lieu.Lieu.dLieux[ligne_proche['LieuB']]
        
        def charger_graph(self, fichier):
            df = pandas.read_csv(fichier)
            return df.values

        def sauvegarder_graph(self, fichier):
            df = pandas.DataFrame(self.liste_lieux)
            df.to_csv(fichier)