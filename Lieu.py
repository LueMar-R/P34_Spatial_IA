class Lieu:
    """Cette classe sert à mémoriser les coordonnées x et y du lieu à visiter."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Lieu : x = {}, y = {}>".format(self.x, self.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, b):
        self.x == b.x
        self.y == y
    
    def distance(self, b):
        """fonction de calcul de distance euclidienne entre 2 lieux."""
        ((self.x - b.x)**2 + (self.y - b.y)**2)**0.5

if __name__ == "__main__":
    import random
    from matplotlib import pyplot as plt

    xt = random.randint(-20, 20)
    yt = random.randint(-20, 20)

    pt = Lieu(xt, yt)

    print(pt1)

    plt.plot(pt1.x, pt1.y, marker="o", color="blue")
    plt.show()