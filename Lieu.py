class Lieu:
    """Cette classe sert à mémoriser les coordonnées x et y du lieu à visiter."""
    dLieux = {} # liste complète des lieux sous forme de dictionnaire
    a_id = 0 # id disponible actuelle

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = Lieu.a_id
        Lieu.dLieux[Lieu.a_id] = self
        Lieu.a_id+=1

    def __repr__(self):
        return "<Lieu : id = {}, x = {}, y = {}>".format(self.id, self.x, self.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def distance(self, b):
        """fonction de calcul de distance euclidienne entre 2 lieux."""
        ((self.x - b.x)**2 + (self.y - b.y)**2)**0.5

if __name__ == "__main__":
    import random
    from matplotlib import pyplot as plt

    xt1 = random.randint(-20, 20)
    yt1 = random.randint(-20, 20)

    pt1 = Lieu(xt1, yt1)

    print("{}".format(pt1))

    plt.plot(pt1.x, pt1.y, marker="o", color="blue")
    plt.show()