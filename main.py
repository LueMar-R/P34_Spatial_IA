import tkinter.messagebox
import tkinter as tk

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1300x760")
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
        canvas.create_rectangle((100, 100), (600, 600), outline="blue", width = 2)



def geomatique():

  app=Application()
  app.mainloop()


geomatique()