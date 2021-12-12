#Permet l'import de Gui pour le type hinting sans créer de problème d'import cyclique :
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.pages.Gui import Gui

from tkinter import Button, Frame, PhotoImage
from tkinter.messagebox import askyesno

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#Classe représentant l'interface du menu :
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
class Menu (Frame):
    #----------------------------------------------------------------------------------------------------------------------------------
    #Constructeur :
    #----------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, parent : Frame, controller : Gui, bg : str) -> None :
        #J'initialise le parent :
        Frame.__init__(self, parent, bg=bg)

        #ATTRIBUTS :

        #Représente le controller (Gui) :
        self.controller = controller
        
        #INIT :
        self.draw()

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction dessinant l'interface du menu :
    #----------------------------------------------------------------------------------------------------------------------------------
    def draw(self) -> None :
        NewGameButton_image = PhotoImage(file=self.controller.relative_to_assets("NewGame.png"))
        NewGameButton = Button(self,cursor="hand2", image=NewGameButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Game"),relief="flat")
        NewGameButton.image=NewGameButton_image
        NewGameButton.place( x=389.0, y=96.0, width=423.0, height=92.0)

        OptionsButton_image = PhotoImage(file=self.controller.relative_to_assets("Options.png"))
        OptionsButton = Button(self,cursor="hand2", image=OptionsButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Options"),relief="flat")
        OptionsButton.image=OptionsButton_image
        OptionsButton.place(x=389.0,y=235.0,width=423.0,height=92.0)

        CreditsButton_image = PhotoImage(file=self.controller.relative_to_assets("Credits.png"))
        CreditsButton = Button(self,cursor="hand2", image=CreditsButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Credits"),relief="flat")
        CreditsButton.image=CreditsButton_image
        CreditsButton.place(x=389.0,y=374.0,width=423.0,height=92.0)

        QuitButton_image = PhotoImage(file=self.controller.relative_to_assets("Quit.png"))
        QuitButton = Button(self, cursor="hand2", image=QuitButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.quit(),relief="flat")
        QuitButton.image=QuitButton_image
        QuitButton.place(x=389.0,y=513.0,width=423.0,height=92.0)
            
    
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de demander la fin de l'execution du script :
    #----------------------------------------------------------------------------------------------------------------------------------
    def quit(self) -> None :
        answer = askyesno(title='Quitter', message='Etes vous sûr de vouloir quitter ?')

        if answer :
            self.controller.quit()