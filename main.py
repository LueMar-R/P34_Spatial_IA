import tkinter.messagebox
import tkinter as tk
from tsp_graph_init import *

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1300x750")
        self.create_widget()
        self.v=tk.IntVar()


    def create_widget(self):
                
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        """Titre"""
        self.champ_titre=tk.Label(self,text="Géomatique",padx="10",pady="10")
        self.champ_titre.config(font=("Helvetica", 44), fg='#7be50a')
        self.champ_titre.pack(side="top")

        """Appel des fonctions"""
        self.pageAcceuil()


    def pageAcceuil(self):
        """Fenêtre principale"""
        self.appli=tk.Frame(self)
        self.appli.config(bg = '#cdcdcd')
        self.appli.pack(fill ="both", expand="yes")
        self.afficher_graph()


    def afficher_graph(self):
        for widget in self.appli.winfo_children():
            widget.destroy()
        self.canvas = tk.Canvas(self.appli, width=800, height=800, bg = 'white')
        self.canvas.pack()  
        self.draw_graph(self.canvas) #appel à la fonction draw_graph


    def draw_graph(self, canvas):  #fonction qui dessine le graphe
        #self.canvas.create_rectangle((10, 10), (790, 660), outline="blue", width = 2) #dessine l'air d'affichage des points


        self.liste_lieux = Graph.creer_liste_lieux()

        #dessin des routes entre les points, les routes sont dessiner avant pour qu'elle ne se dessine pas dans les ronds
        for x in range(len(self.liste_lieux)):
            try:
                self.canvas.create_line((self.liste_lieux[x][0], self.liste_lieux[x][1]), ((self.liste_lieux[x+1][0]), (self.liste_lieux[x+1][1])), width = 1, fill = 'blue')
            except IndexError:
                self.canvas.create_line((self.liste_lieux[x][0], self.liste_lieux[x][1]), ((self.liste_lieux[0][0]), (self.liste_lieux[0][1])), width = 1, fill = 'blue')

        #boucle for qui dessine les points et écrit le numéro à l'interieur        
        for x in range(len(self.liste_lieux)):
            if x == 0:
                color = 'red'
            else:
                color = 'white'
            self.canvas.create_oval((self.liste_lieux[x][0]-7, self.liste_lieux[x][1]-7), ((self.liste_lieux[x][0]+7), (self.liste_lieux[x][1]+7)), width = 1, fill = color)
            self.canvas.create_text((self.liste_lieux[x][0], self.liste_lieux[x][1]),text=x)







def geomatique():

  app=Application()
  app.mainloop()


geomatique()