#Permet l'import de Player et de Gui pour le type hinting sans créer de problème d'import cyclique :
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.logic.Player import Player
    from src.pages.Gui import Gui
    
from tkinter import Button, Frame, PhotoImage, Label, Radiobutton, IntVar, StringVar, Toplevel
from tkinter.messagebox import askyesno
from src.logic.GameCtrl import GameCtrl

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#Classe représentant l'interface d'une partie :
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
class Game (Frame):
    #----------------------------------------------------------------------------------------------------------------------------------
    #Constructeur :
    #----------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, parent : Frame, controller : Gui, bg : str) -> None :
        #J'initialise le parent :
        Frame.__init__(self, parent, bg=bg)

        #ATTRIBUTS :

        #Couleur de fond :
        self.bg = bg
        #Représente le controller (Gui) :
        self.controller = controller
        #Représente le controller de jeu (contenant toute la logique) :
        self.gameCtrl = None
        #Représente une grille 3*3 (où seront stockés les boutons)
        self.gridCase=[]
        #Représente le type de gobelet sélectionné par le joueur sur l'interface (-> pour l'interface)
        self.goblet_type = IntVar()
        #Représente le nombre de petits gobelets restants (-> pour l'interface):
        self.nbLittleGobletRestant = StringVar()
        #Représente le nombre de gobelets moyens restants (-> pour l'interface):
        self.nbMediumGobletRestant = StringVar()
        #Représente le nombre de gros gobelets restants (-> pour l'interface) :
        self.nbBigGobletRestant = StringVar()
        #Permet de représenter à quel joueur est-ce au tour de jouer (-> pour l'interface) :
        self.tourLabel = StringVar()
        
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction lançant une nouvelle partie de jeu :
    #----------------------------------------------------------------------------------------------------------------------------------
    def newGame (self) -> None :
        #On initialise le controller logique :
        self.gameCtrl = GameCtrl()
        #On lance une nouvelle partie
        self.gameCtrl.newGame()
        #On dessine l'interface
        self.drawPage()
        #On initialise le choix du gobelet à moyen :
        self.goblet_type.set(2)
        #on met à jour les elements d'interface :
        self.updateNbGoblet()
        self.updateTourLabel()
        self.updatePreviewGoblet()

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction dessinant l'interface de jeu :
    #----------------------------------------------------------------------------------------------------------------------------------
    def drawPage(self) -> None :
        #Titre de la page :
        title = Label(self, anchor="nw",text="Partie en cours",bg=self.bg, fg="white", font=("Roboto Bold", 40 * -1))
        title.place(x=437.0, y=16.0)

        #GameSettingView :
        SettingsView = Label(self, anchor="nw", justify="left",text=f"Mode : {self.gameCtrl.game_type}\nIA : {self.gameCtrl.ia_level}\n",bg=self.bg, fg="#FFFFFF", font=("Roboto Bold", 14 * -1))
        SettingsView.place(x=13.0, y=14.0)

        #Tour :
        tour = Label(self, anchor="nw",textvariable=self.tourLabel,bg=self.bg, fg="#F4F6D9", font=("Roboto Bold", 32 * -1))
        tour.place(x=400.0, y=90.0)

        #Gobelets title
        GobeletTitle = Label(self, anchor="nw", text="Gobelets :",bg=self.bg, fg="#F4F6D9", font=("Roboto Bold", 32 * -1))
        GobeletTitle.place(x=875.0, y=134.0)

        #Choix de la taille du gobelet :
        little_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Petit :", variable=self.goblet_type, value=1, command=lambda:self.updateSelectGoblet(), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9", selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
        little_RadioButton.place(x=757, y=234)
        medium_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Moyen :", variable=self.goblet_type, value=2, command=lambda:self.updateSelectGoblet(), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9",  selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
        medium_RadioButton.place(x=727, y=349)
        big_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Grand :", variable=self.goblet_type, value=3, command=lambda:self.updateSelectGoblet(), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9",  selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
        big_RadioButton.place(x=737, y=464)

        #NbRestants de gobelets :
        little_restants = Label(self, anchor="nw", textvariable=self.nbLittleGobletRestant,bg=self.bg, fg="#F4F6D9", font=("Roboto Medium", 27 * -1))
        little_restants.place(x=870, y=236)
        medium_restants = Label(self, anchor="nw",textvariable=self.nbMediumGobletRestant,bg=self.bg, fg="#F4F6D9", font=("Roboto Medium", 27 * -1))
        medium_restants.place(x=870, y=351)
        big_restants = Label(self, anchor="nw",textvariable=self.nbBigGobletRestant,bg=self.bg, fg="#F4F6D9", font=("Roboto Medium", 27 * -1))
        big_restants.place(x=870, y=466)

        #Emplacement pour l'image des Gobelets :
        self.littleGobelet_preview = Label(self, bg=self.bg)
        self.littleGobelet_preview.place(x=1058, y = 236)

        self.mediumGobelet_preview = Label(self, bg=self.bg)
        self.mediumGobelet_preview.place(x=1051, y = 347)

        self.bigGobelet_preview = Label(self, bg=self.bg)
        self.bigGobelet_preview.place(x=1050, y = 445)

        #On dessine la grille :
        self.drawGrid()

        #Boutton pour quitter :
        QuitButton_image = PhotoImage(file=self.controller.relative_to_assets("QuitGame.png"))
        QuitButton = Button(self, cursor="hand2", image=QuitButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.quitGame(),relief="flat")
        QuitButton.image=QuitButton_image
        QuitButton.place(x=455.0,y=624.0,width=290.0,height=55.0)
        
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction dessinant la grille de jeu :
    #----------------------------------------------------------------------------------------------------------------------------------
    def drawGrid(self, ) -> None :
        EmptyCase_image = PhotoImage(file=self.controller.relative_to_assets("EmptyCase.png"))

        col1Pos = 140.0
        col2Pos = 262.0
        col3Pos = 384.0

        line1Pos = 195.0
        line2Pos = 317.0
        line3Pos = 439.0

        #Colonne 0 :
        L0C0 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(0,0),relief="flat")
        L0C0.image=EmptyCase_image
        L0C0.place(x=col1Pos,y=line1Pos,width=105.0,height=105.0)

        L1C0 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(1,0),relief="flat")
        L1C0.image=EmptyCase_image
        L1C0.place(x=col1Pos,y=line2Pos,width=105.0,height=105.0)

        L2C0 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(2,0),relief="flat")
        L2C0.image=EmptyCase_image
        L2C0.place(x=col1Pos,y=line3Pos,width=105.0,height=105.0)

        #Colonne 2 :
        L0C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(0,1),relief="flat")
        L0C1.image=EmptyCase_image
        L0C1.place(x=col2Pos,y=line1Pos,width=105.0,height=105.0)

        L1C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(1,1),relief="flat")
        L1C1.image=EmptyCase_image
        L1C1.place(x=col2Pos,y=line2Pos,width=105.0,height=105.0)

        L2C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(2,1),relief="flat")
        L2C1.image=EmptyCase_image
        L2C1.place(x=col2Pos,y=line3Pos,width=105.0,height=105.0)

        #Colonne 3 :
        L0C2 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(0,2),relief="flat")
        L0C2.image=EmptyCase_image
        L0C2.place(x=col3Pos,y=line1Pos,width=105.0,height=105.0)

        L1C2 = Button(self,  image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(1,),relief="flat")
        L1C2.image=EmptyCase_image
        L1C2.place(x=col3Pos,y=line2Pos,width=105.0,height=105.0)

        L2C2 = Button(self,  image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(2,2),relief="flat")
        L2C2.image=EmptyCase_image
        L2C2.place(x=col3Pos,y=line3Pos,width=105.0,height=105.0)

        self.gridCase=[[L0C0, L0C1, L0C2],
                       [L1C0, L1C1, L1C2],
                       [L2C0, L2C1, L2C2]]

        return None

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de déclencher la demande de jouer une combinaison par un joueur (lorsqu'il clique sur une des cases de la grille) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def pressCase(self, line : int, column : int) -> None :
        #Si la combinaison est valide :
        if self.gameCtrl.actual_player.play(line, column) :
            #On met à jour la grille et le nb de gobelets restants :
            self.updateGrid()
            self.updateNbGoblet()

            #S'il n'y a pas de gagnants :
            if not(self.checkWin()) :
                #On passe le tour :
                self.gameCtrl.nextTurn()
                #On remet à jour la grille et on revérifie s'il y a un gagnant (utilise puisque l'IA à jouer dans la foulée)
                self.updateGrid()
                self.checkWin()
                #On met à jour les autres elements d'interfaces :
                self.updateSelectGoblet()
                self.updateNbGoblet()
                self.updateTourLabel()
                self.updatePreviewGoblet()
        return None

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de déclencher l'ouverture de la fenêtre de victoire s'il y a un gagnant :
    #----------------------------------------------------------------------------------------------------------------------------------
    def checkWin(self) -> bool :
        if self.gameCtrl.isWin(self.gameCtrl.player_1) :
            self.winPopup(self.gameCtrl.player_1)
            return True
        elif self.gameCtrl.isWin(self.gameCtrl.player_2) :
            self.winPopup(self.gameCtrl.player_2)
            return True
        else :
            return False

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction dessinant la fenêtre de victoire :
    #----------------------------------------------------------------------------------------------------------------------------------
    def winPopup(self, player : Player) -> bool :
        winPopup = Toplevel(self)
        winPopup.title("Victoire !")
        winPopupBgColor = "#4C5985"
        winPopup.configure(background=winPopupBgColor)
        #Taille de la fenêtre
        winPopupWidth = 500
        winPopupHeight = 192
        winPopup.geometry(f"{winPopupWidth}x{winPopupHeight}")
        #Positition de la fenêtre pour la centrer
        x_Left = int(winPopup.winfo_screenwidth()/2 - winPopupWidth/2)
        y_Top = int(winPopup.winfo_screenheight()/2 - winPopupHeight/2)
        
        #Centrage de la fenêtre
        winPopup.geometry("+{}+{}".format(x_Left, y_Top))
        #Empêche de fermer la fenêtre :
        winPopup.protocol("WM_DELETE_WINDOW", lambda:None)
        winPopup.overrideredirect(True)
        winPopup.grab_set()
        
        labelExample = Label(winPopup, text = "Victoire du joueur "+str(player.id)+" !", bg=winPopupBgColor, fg="#FFFFFF", font=("Roboto Bold", 40 * -1))
        labelExample.place(x= 58, y = 33)
        ReturnMenu_image = PhotoImage(file=self.controller.relative_to_assets("ReturnMenuAfterWin.png"))
        ReturnMenuButton = Button(winPopup, cursor="hand2", image=ReturnMenu_image,borderwidth=0,highlightthickness=0,command=lambda: self.afterWin(),relief="flat")
        ReturnMenuButton.image=ReturnMenu_image
        ReturnMenuButton.place(x=100.0,y=111.0,width=299.0,height=54.0)

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de revenir au menu et de supprimer le contenu de la partie après une victoire :
    #----------------------------------------------------------------------------------------------------------------------------------
    def afterWin(self) -> None :
        self.controller.show_frame("Menu")
        self.deleteContent()

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction mettant à jour les aperçus des gobelets de l'interface (à droite) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def updatePreviewGoblet(self) -> None :
        idPlayer = self.gameCtrl.actual_player.id

        littleGobeletImage= PhotoImage(file=self.controller.relative_to_assets(str(idPlayer)+"_LittleGoblet.png"))
        self.littleGobelet_preview["image"] = littleGobeletImage
        self.littleGobelet_preview.image = littleGobeletImage

        mediumGobeletImage= PhotoImage(file=self.controller.relative_to_assets(str(idPlayer)+"_MediumGoblet.png"))
        self.mediumGobelet_preview["image"] = mediumGobeletImage
        self.mediumGobelet_preview.image = mediumGobeletImage

        bigGobeletImage= PhotoImage(file=self.controller.relative_to_assets(str(idPlayer)+"_BigGoblet.png"))
        self.bigGobelet_preview["image"] = mediumGobeletImage
        self.bigGobelet_preview.image = bigGobeletImage

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction mettant à jour l'annonce du tour :
    #----------------------------------------------------------------------------------------------------------------------------------
    def updateTourLabel(self) -> None :
        self.tourLabel.set("C'est au tour du joueur "+str(self.gameCtrl.actual_player.id)+" !")

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction mettant à jour les aperçus des gobelets de l'interface (à droite) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def updateNbGoblet(self) -> None :
        self.nbLittleGobletRestant.set(str(self.gameCtrl.actual_player.nbLittleGoblets)+" restants")
        self.nbMediumGobletRestant.set(str(self.gameCtrl.actual_player.nbMediumGoblets)+" restants")
        self.nbBigGobletRestant.set(str(self.gameCtrl.actual_player.nbBigGoblets)+" restants")

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction mettant à jour la grille de jeu :
    #----------------------------------------------------------------------------------------------------------------------------------
    def updateGrid(self) -> None :
        for line in range(len(self.gameCtrl.grid)) :
            for column in range(len(self.gameCtrl.grid[line])) :
                player = self.gameCtrl.grid[line][column]["player"]
                goblet = self.gameCtrl.grid[line][column]["goblet"]
                self.updateImageCase(self.gridCase[line][column], player, goblet)

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de changer l'image d'une case :
    #----------------------------------------------------------------------------------------------------------------------------------
    def updateImageCase(self, button : Button, player : Player, goblet : int) -> None :
        if goblet == 0 :
            return None
        elif goblet == 1 :
            gobletName = "LittleGobletCase"
        elif goblet == 2 :
            gobletName = "MediumGobletCase"
        elif goblet == 3 :
            gobletName = "BigGobletCase"

        gobletImagePath = str(player.id)+"_"+gobletName+".png"
        ImageCase = PhotoImage(file=self.controller.relative_to_assets(gobletImagePath))
        button['image'] = ImageCase
        button.image = ImageCase

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de mettre à jour le gobelet sélectionné coté logique :
    #----------------------------------------------------------------------------------------------------------------------------------
    def updateSelectGoblet(self) -> None :
        self.gameCtrl.actual_player.selectGoblet(self.goblet_type.get())
        return None

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de quitter la partie :
    #----------------------------------------------------------------------------------------------------------------------------------
    def quitGame(self) -> None :
        print('quitGame')
        answer = askyesno(title='Quitter', message='Etes vous sûr de vouloir quitter ?\nLa partie ne sera pas sauvegardée.')

        if answer :
            self.controller.show_frame("Menu")
            self.deleteContent()

        return None
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de supprimer le contenu de l'interface de jeu :
    #----------------------------------------------------------------------------------------------------------------------------------
    def deleteContent(self) -> None :
        for child in self.winfo_children() :
            child.destroy()

        return None
