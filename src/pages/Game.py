from tkinter import Button, Frame, PhotoImage, Label, Radiobutton, IntVar
from tkinter.constants import N
from tkinter.messagebox import NO, askyesno
from src.logic.GameCtrl import GameCtrl



class Game (Frame):
    def __init__(self, parent, controller, bg) -> None :
        Frame.__init__(self, parent, bg=bg)

        #attributes :
        self.bg = bg
        self.controller = controller
        self.gameCtrl = None
        self.game_type = None
        self.ia_level = None
        self.gridCase=[]

        self.goblet_type = IntVar()
        self.goblet_type.set(2)
        

    def newGame (self) -> None :
        self.gameCtrl = GameCtrl()
        self.game_type = self.gameCtrl.game_type
        self.ia_level = self.gameCtrl.ia_level

        self.drawPage()
        self.gameCtrl.newGame()

    def drawPage(self) -> None :
        #Titre de la page :
        title = Label(self, anchor="nw",text="Partie en cours",bg=self.bg, fg="white", font=("Roboto Bold", 40 * -1))
        title.place(x=437.0, y=16.0)

        #GameSettingView :
        SettingsView = Label(self, anchor="nw", justify="left",text=f"Mode : {self.game_type}\nIA : {self.ia_level}\n",bg=self.bg, fg="#FFFFFF", font=("Roboto Bold", 14 * -1))
        SettingsView.place(x=13.0, y=14.0)

        #Tour :
        tour = Label(self, anchor="nw",text="C'est au tour du joueur 1 !",bg=self.bg, fg="#F4F6D9", font=("Roboto Bold", 32 * -1))
        tour.place(x=400.0, y=90.0)

        #Gobelets title
        GobeletTitle = Label(self, anchor="nw", text="Gobelets :",bg=self.bg, fg="#F4F6D9", font=("Roboto Bold", 32 * -1))
        GobeletTitle.place(x=875.0, y=134.0)

        #Choix de la taille du gobelet :
        little_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Petit :", variable=self.goblet_type, value=1, command=lambda:self.updatePlayer(), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9", selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
        little_RadioButton.place(x=757, y=234)
        medium_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Moyen :", variable=self.goblet_type, value=2, command=lambda:self.updatePlayer(), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9",  selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
        medium_RadioButton.place(x=727, y=349)
        big_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Grand :", variable=self.goblet_type, value=3, command=lambda:self.updatePlayer(), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9",  selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
        big_RadioButton.place(x=737, y=464)

        #NbRestants de gobelets :
        little_restants = Label(self, anchor="nw", text="2 restants",bg=self.bg, fg="#F4F6D9", font=("Roboto Medium", 27 * -1))
        little_restants.place(x=870, y=236)
        medium_restants = Label(self, anchor="nw",text="3 restants",bg=self.bg, fg="#F4F6D9", font=("Roboto Medium", 27 * -1))
        medium_restants.place(x=870, y=351)
        big_restants = Label(self, anchor="nw",text="2 restants",bg=self.bg, fg="#F4F6D9", font=("Roboto Medium", 27 * -1))
        big_restants.place(x=870, y=466)



        #On dessine la grille :
        self.drawGrid()


        QuitButton_image = PhotoImage(file=self.controller.relative_to_assets("QuitGame.png"))
        QuitButton = Button(self, cursor="hand2", image=QuitButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.quitGame(),relief="flat")
        QuitButton.image=QuitButton_image
        QuitButton.place(x=455.0,y=624.0,width=290.0,height=55.0)
        
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

        L1C2 = Button(self,  image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(1,2),relief="flat")
        L1C2.image=EmptyCase_image
        L1C2.place(x=col3Pos,y=line2Pos,width=105.0,height=105.0)

        L2C2 = Button(self,  image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: self.pressCase(2,2),relief="flat")
        L2C2.image=EmptyCase_image
        L2C2.place(x=col3Pos,y=line3Pos,width=105.0,height=105.0)



        return None

    def pressCase(self, line : int, column : int) -> None :
        self.gameCtrl.actual_player.play(line, column)

        return None

    def updatePlayer(self) -> None :
        self.gameCtrl.actual_player.selectGoblet(self.goblet_type.get())
        return None

    def quitGame(self) -> None :
        print('quitGame')
        answer = askyesno(title='Quitter', message='Etes vous sûr de vouloir quitter ?\nLa partie ne sera pas sauvegardée.')

        if answer :
            self.controller.show_frame("Menu")
            self.deleteContent()

        return None
    
    def deleteContent(self) -> None :
        for child in self.winfo_children() :
            child.destroy()

        return None
