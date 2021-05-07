import random

class Lieu:
    def __init__(self):
        return None

    def definir(self, x, y):
        x = float(x)
        y = float(y)
        return {"x":x, "y":y}

    def calc_distance(self, lieu_1, lieu_2):
        x_1 = lieu_1["x"]
        y_1 = lieu_1["y"]
        x_2 = lieu_2["x"]
        y_2 = lieu_2["y"]

        distance_x = abs(x_1 - x_2)
        distance_y = abs(y_1 - y_2)
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
            x = random.uniform(0, largeur)
            y = random.uniform(0, hauteur)
            lieu = Lieu().definir(x, y)

            liste_lieux.append(lieu)

        return liste_lieux

print(Graph().liste_lieux(10, 20, 3))