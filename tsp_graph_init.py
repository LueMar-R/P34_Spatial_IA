import random
import numpy as np

class Lieu:
    def __init__(self):
        return None

    def definir(self, nom, x, y):
        nom = str(nom)
        x = float(x)
        y = float(y)
        return {"nom":nom, "x":x, "y":y}

    def calc_distance(self, lieu_1, lieu_2):
        x_1 = lieu_1["x"]
        y_1 = lieu_1["y"]
        x_2 = lieu_2["x"]
        y_2 = lieu_2["y"]

        distance_x = x_1 - x_2
        distance_y = y_1 - y_2
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
        return distance


class Graph:
    def __init__(self):
        return None

    def liste_lieux(self, largeur, hauteur, nb_lieux):
        liste_lieux = []
        largeur = float(largeur)
        hauteur = float(hauteur)
        nb_lieux = int(nb_lieux)

        for i in range(nb_lieux):
            nom = "lieu " + str(i+1)
            x = random.uniform(0, largeur)
            y = random.uniform(0, hauteur)
            lieu = Lieu().definir(nom, x, y)

            liste_lieux.append(lieu)

        return liste_lieux
    
    def calcul_matrice_cout_od(self, liste_lieux):
        liste_lieux_2 = liste_lieux.copy()
        matrice_od = []
        for lieu in liste_lieux:
            liste_lieux_2.remove(lieu)
            for lieu_2 in liste_lieux_2:
                distance = Lieu().calc_distance(lieu, lieu_2)
                dict_distance = {"l1":lieu["nom"], "l2":lieu_2["nom"], "distance":distance}
                matrice_od.append(dict_distance)
        return matrice_od

    def plus_proche_voisins(self, matrice, lieu):
        lieu = str(lieu)
        liste_dicts = []
        for item in matrice:
            if item["l1"] == lieu:
                liste_dicts.append({"lieu":item["l2"], "distance":item["distance"]})
            elif item["l2"] == lieu:
                liste_dicts.append({"lieu":item["l1"], "distance":item["distance"]})
                
        plus_petite_distance = min([dico["distance"] for dico in liste_dicts])
        plus_proche_voisins = []
        for dico in liste_dicts:
            if dico["distance"] == plus_petite_distance:
                plus_proche_voisins.append(dico)
        return plus_proche_voisins
        

liste_lieux = Graph().liste_lieux(10, 20, 4)
matrice_od = Graph().calcul_matrice_cout_od(liste_lieux)
print(Graph().plus_proche_voisins(matrice_od, "lieu 1"))
