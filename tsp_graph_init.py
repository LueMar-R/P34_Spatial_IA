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

lieu_A = Lieu().definir(1, 2)
lieu_B = Lieu().definir(5, 6)

distance_AB = Lieu().calc_distance(lieu_A, lieu_B)
print(distance_AB)