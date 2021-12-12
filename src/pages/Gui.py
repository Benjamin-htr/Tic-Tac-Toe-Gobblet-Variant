from tkinter import Tk, Frame
from src.pages.Options import Options
from src.pages.Menu import Menu
from src.pages.Credits import Credits
from src.pages.Game import Game

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#Classe représentant le controlleur de l'interface :
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
class Gui(Tk) :
    #----------------------------------------------------------------------------------------------------------------------------------
    #Constructeur :
    #----------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs) -> None:
        #Initialisation de la fenêtre principale :
        Tk.__init__(self, *args, **kwargs)
        #On empêche le fait de pouvoir régler la taille de la fenêtre :
        self.resizable(False, False)

        #ATTRIBUTS :

        #Chemin d'accès aux ressources images :
        self.assets_path = "./assets"
        #Titre de la fenêtre :
        self.title('Tic tac toe')
        #Taille de la fenêtre :
        self.geometry('1200x700')
        #Couleur de fond de l'interface :
        self.bg = "#6992FC"
        #Différentes possibles :
        self.pages=[Menu, Options, Credits, Game]

        #Création d'un conteneur :
        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        #Grille (utile pour bien positionner les différentes pages)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        #Représente les différentes pages possibles (et initialisés) :
        self.frames = {} 
        #Pour chaque page possible :
        for F in (self.pages):
            #Je récupère son nom :
            page_name = F.__name__
            #Je l'initialise :
            frame = F(parent=container, controller=self, bg=self.bg)
            #Je l'ajoute :
            self.frames[page_name] = frame
            #Je la positionne :
            frame.grid(row = 0, column = 0, sticky ="nsew")

        #Page de départ : Menu :
        self.show_frame("Menu")


    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant d'afficher la page dont le nom est entré en paramètre :
    #----------------------------------------------------------------------------------------------------------------------------------
    def show_frame(self, page_name : str):
        print("Go to : "+page_name)
        frame = self.frames[page_name]
        frame.tkraise()
        
        #Si je clique sur "Nouvelle Partie"
        if page_name == "Game" :
            #On lance la partie
            frame.newGame() 

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de fermer la fenêtre et de terminer l'exécution du script :
    #----------------------------------------------------------------------------------------------------------------------------------
    def closeApp(self) -> None :
        self.destroy()
    
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de retourner le chemin vers l'image dont le nom est entré en paramètre :
    #----------------------------------------------------------------------------------------------------------------------------------
    def relative_to_assets(self, path: str) -> str:
            return self.assets_path+"/"+path


        
        
