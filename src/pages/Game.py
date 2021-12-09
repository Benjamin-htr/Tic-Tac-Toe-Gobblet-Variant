from tkinter import Button, Frame, PhotoImage, Label, Radiobutton, StringVar
from tkinter.messagebox import askyesno
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

        self.goblet_type = StringVar()
        self.goblet_type.set("medium")
        

    def newGame (self) -> None :
        self.gameCtrl = GameCtrl()
        self.game_type = self.gameCtrl.game_type
        self.ia_level = self.gameCtrl.ia_level

        self.drawPage()

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
        little_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Petit :", variable=self.goblet_type, value="little", command=lambda:print("little !"), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9", selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
        little_RadioButton.place(x=757, y=234)
        medium_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Moyen :", variable=self.goblet_type, value="medium", command=lambda:print("medium !"), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9",  selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
        medium_RadioButton.place(x=727, y=349)
        big_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Grand :", variable=self.goblet_type, value="big", command=lambda:print("big !"), activebackground="#557CE0", bg=self.bg, fg="#F4F6D9",  selectcolor="black", activeforeground="#F4F6D9", font=("Roboto Medium", 27 * -1))
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

        #Colonne 1 :
        L1C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L1C1 clicked"),relief="flat")
        L1C1.image=EmptyCase_image
        L1C1.place(x=col1Pos,y=line1Pos,width=105.0,height=105.0)

        L2C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L2C1 clicked"),relief="flat")
        L2C1.image=EmptyCase_image
        L2C1.place(x=col1Pos,y=line2Pos,width=105.0,height=105.0)

        L3C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L3C1 clicked"),relief="flat")
        L3C1.image=EmptyCase_image
        L3C1.place(x=col1Pos,y=line3Pos,width=105.0,height=105.0)

        #Colonne 2 :
        L1C2 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L1C2 clicked"),relief="flat")
        L1C2.image=EmptyCase_image
        
        L1C2.place(x=col2Pos,y=line1Pos,width=105.0,height=105.0)

        L2C2 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L2C2 clicked"),relief="flat")
        L2C2.image=EmptyCase_image
        L2C2.place(x=col2Pos,y=line2Pos,width=105.0,height=105.0)

        L3C2 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L3C2 clicked"),relief="flat")
        L3C2.image=EmptyCase_image
        L3C2.place(x=col2Pos,y=line3Pos,width=105.0,height=105.0)

        #Colonne 3 :
        L1C3 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L1C3 clicked"),relief="flat")
        L1C3.image=EmptyCase_image
        L1C3.place(x=col3Pos,y=line1Pos,width=105.0,height=105.0)

        L2C3 = Button(self,  image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L2C3 clicked"),relief="flat")
        L2C3.image=EmptyCase_image
        L2C3.place(x=col3Pos,y=line2Pos,width=105.0,height=105.0)

        L3C3 = Button(self,  image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L3C3 clicked"),relief="flat")
        L3C3.image=EmptyCase_image
        L3C3.place(x=col3Pos,y=line3Pos,width=105.0,height=105.0)

        return None

    def quitGame(self) -> None :
        print('quitGame')
        answer = askyesno(title='Quitter', message='Etes vous sûr de vouloir quitter ?\nLa partie ne sera pas sauvegardée.')

        if answer :
            self.controller.show_frame("Menu")
            self.deleteContent()
    
    def deleteContent(self) -> None :
        for child in self.winfo_children():
            child.destroy()

        return None
