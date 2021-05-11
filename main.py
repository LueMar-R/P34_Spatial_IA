import tkinter.messagebox
import tkinter as tk
from tsp_graph_init import *
from TSP_SA import *
import time

class Affichage(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1300x800")
        self.create_widget()
        self.v=tk.IntVar()


    def create_widget(self):
                
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        """Titre"""
        self.champ_titre=tk.Label(self,text="Géomatique",padx="10",pady="10")
        self.champ_titre.config(font=("Helvetica", 44), fg='#7be50a')
        self.champ_titre.pack(side="top")

        """Fenêtre principale"""
        self.appli=tk.Frame(self)
        self.appli.config(bg = '#cdcdcd')
        self.appli.pack(fill ="both", expand="yes")
        self.draw_graph(self.appli) #appel à la fonction draw_graph


    def draw_graph(self, canvas):  #fonction qui dessine le graphe
        self.canvas = tk.Canvas(self.appli, width=800, height=700, bg = 'white')
        self.canvas.pack()

        self.TSP = TSP_SA(700, 650, 10)
        self.liste_lieux = self.TSP.graphe.liste_lieux  #appel de la fonction qui créer la liste des lieux

        #création d'un dictionnaire pour y ranger les lieux par numéro, avec leur coordonnées
        self.dico_lieux = {}
        for x in range(len(self.liste_lieux)):
            self.dico_lieux[x] = [self.liste_lieux[x].x, self.liste_lieux[x].y]

  
        #boucle for qui dessine les points et écrit le numéro à l'interieur
        for x in range(len(self.liste_lieux)):
            if x == 0:
                color = 'red'
            else:
                color = 'silver'
            self.canvas.create_oval((self.dico_lieux[x][0]-7, self.dico_lieux[x][1]-7), ((self.dico_lieux[x][0]+7), (self.dico_lieux[x][1]+7)), width = 1, fill = color)
            self.canvas.create_text((self.dico_lieux[x][0], self.dico_lieux[x][1]),text=x)


        # appel de la fonction qui trouve la première route
        self.premiere_route = self.TSP.heuristique()

        for x in self.premiere_route:
            try:
                self.canvas.create_line((self.dico_lieux[self.premiere_route[x]][0], self.dico_lieux[self.premiere_route[x]][1]), ((self.dico_lieux[self.premiere_route[x+1]][0]), (self.dico_lieux[self.premiere_route[x+1]][1])), width = 2, dash=(4), fill = 'blue')
            except KeyError:
                self.canvas.create_line((self.dico_lieux[x][0], self.dico_lieux[x][1]), ((self.dico_lieux[0][0]), (self.dico_lieux[0][1])), width = 2, dash=(4), fill = 'blue')
            canvas.update()
                 
        
        # affichage du texte en bas de la fenêtre TK
        self.affichage_distance = tk.Label(self.appli,text='distance : '+ str(self.TSP.distance_zero),padx="10",pady="10")
        self.affichage_distance.pack()


def geomatique():

  app=Affichage()
  app.mainloop()


geomatique()