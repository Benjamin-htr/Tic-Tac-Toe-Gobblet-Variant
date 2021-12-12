#Permet l'import de Gui pour le type hinting sans créer de problème d'import cyclique :
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.pages.Gui import Gui

from tkinter import Button, Frame, PhotoImage, Label
from webbrowser import open_new_tab

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#Classe représentant l'interface des crédits :
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
class Credits (Frame):
    #----------------------------------------------------------------------------------------------------------------------------------
    #Constructeur :
    #----------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, parent : Frame, controller : Gui, bg : str) -> None :
        #J'initialise le parent :
        Frame.__init__(self, parent, bg=bg)
        
        #ATTRIBUTS :

        #Représente la couleur du fond
        self.bg = bg
        #Représente le controller (Gui) :
        self.controller = controller
        
        #INIT :
        self.draw()

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction dessinant l'interface :
    #----------------------------------------------------------------------------------------------------------------------------------
    def draw(self) -> None :
        title = Label(self, anchor="nw", justify="center",text="Crédits",bg=self.bg, fg="white", font=("Roboto Bold", 44 * -1))
        title.place(x=514, y=13)

        name = Label(self, anchor="nw",text="Developpeur : Hautier Benjamin", bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 30 * -1))
        name.place(x=382.0, y=71.0)

        versions = Label(self,anchor="nw", text="Version de python : 3.9.1",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 30 * -1))
        versions.place(x=431.0, y=128.0)

        librairies = Label(self,anchor="nw", text="Librairies (normalement inclus de base dans python) :",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 30 * -1))
        librairies.place(x=234, y=175)

        tkinter = Label(self,anchor="nw", text="-Tkinter (v8.6)",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 23 * -1))
        tkinter.place(x=524.0, y=219.0)

        configParser = Label(self,anchor="nw", text="-ConfigParser",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 23 * -1))
        configParser.place(x=526.0, y=256.0)

        os = Label(self,anchor="nw", text="-Os",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 23 * -1))
        os.place(x=527.0, y=293.0)

        Random = Label(self,anchor="nw", text="-Random",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 23 * -1))
        Random.place(x=521.0, y=330.0)

        future = Label(self,anchor="nw", text="-__Future__",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 23 * -1))
        future.place(x=525.0, y=367.0)

        typing = Label(self,anchor="nw", text="-typing",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 23 * -1))
        typing.place(x=522.0, y=404.0)

        webbrowser = Label(self,anchor="nw", text="-Webbrowser",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 23 * -1))
        webbrowser.place(x=514.0, y=441.0)

        git = Label(self,anchor="nw",text="Repository github :",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 30 * -1)) 
        git.place(x=471.0, y=491.0)

        githubLink = "https://github.com/Benjamin-htr/Tic-Tac-Toe-Gobblet-Variant"
        #Fonction pour ouvrir lien github :
        def callback(url):
            open_new_tab(url)
        gitLink = Label(self,anchor="nw",cursor="hand2", text=githubLink,bg=self.bg, fg="#3500CC",activeforeground="#7200CC",font=("Roboto Medium", 26 * -1, 'underline'))
        gitLink.place(x=240.0, y=536.0)
        gitLink.bind("<Button-1>", lambda e:callback(githubLink))
        

        ReturnMenu_image = PhotoImage(file=self.controller.relative_to_assets("ReturnMenu.png"))
        ReturnMenuButton = Button(self, cursor="hand2", image=ReturnMenu_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Menu"),relief="flat")
        ReturnMenuButton.image=ReturnMenu_image
        ReturnMenuButton.place(x=388.0,y=590.0,width=423.0,height=92.0)
