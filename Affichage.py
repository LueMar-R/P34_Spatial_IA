from Graph import Graph
from tkinter import *

LARGEUR = 800
HAUTEUR = 600

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=LARGEUR, height=800, **kwargs)
        fenetre.title("groupe 6")

        fenetre.bind_all('<Escape>', fenetre.quit)

        self.graph = Graph(10, LARGEUR, HAUTEUR)
        rayonPoints = 10

        self.canvas = Canvas(fenetre, width=LARGEUR, height=HAUTEUR, bg="white")
        self.canvas.pack()

        self.graph.calcul_matrice_cout_od()
        for i in Graph.matrice_od.index: 
            self.canvas.create_line((Graph.matrice_od["LieuA"][i].x, Graph.matrice_od["LieuA"][i].y), (Graph.matrice_od["LieuB"][i].x, Graph.matrice_od["LieuB"][i].y), 
                        fill="gray", width=3)
        
        
        for i, lieu in enumerate(self.graph.liste_lieux):
            self.canvas.create_oval((lieu.x - rayonPoints, lieu.y - rayonPoints), (lieu.x + rayonPoints, lieu.y + rayonPoints), 
                            fill="silver", outline="black", width=3)
            self.canvas.create_text(lieu.x, lieu.y, text=str(i),
                            fill="black", font= ("courier", 10, "bold italic"),
                            anchor="center", justify= "center")
        
        
        
        self.evol = Label(fenetre, text="{}".format(self.graph))
        self.evol.pack()

fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()