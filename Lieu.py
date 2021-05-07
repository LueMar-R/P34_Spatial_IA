class Lieu:
    """Cette classe sert à mémoriser les coordonnées x et y du lieu à visiter."""
    dLieux = {} # liste complète des lieux sous forme de dictionnaire
    a_id = 0 # id disponible actuelle

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = a_id
        Lieu.dLieux[a_id] = self
        Lieu.a_id+=1

    def distance(self, b):
        ((self.x - b.x)**2 + (self.y - b.y)**2)**0.5