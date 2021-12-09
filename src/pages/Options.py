from tkinter import Button, Frame, PhotoImage, Label, Radiobutton, StringVar
from src.logic.configCtrl import configCtrl

class Options (Frame):
    def __init__(self, parent, controller, bg) -> None :
        Frame.__init__(self, parent, bg=bg)
        
        #attributes :
        self.bg = bg
        self.controller = controller
        self.gameType = StringVar()
        self.iaLevel = StringVar()
        

        self.configCtrl = configCtrl()
        
        #init :
        self.draw()
        self.initCoices()

    #fonction mettant à jour l'interface par rapport au fichier de config
    def initCoices(self) :
        game_type_stored = self.configCtrl.getGame_type()
        ia_level_stored = self.configCtrl.getIa_level()

        self.gameType.set(game_type_stored)
        self.iaLevel.set(ia_level_stored)

    #fonction mettant à jour le fichier de config
    def updateConfig(self) :
        self.configCtrl.updateConfig(self.gameType.get(), self.iaLevel.get())

    def showGameType(self) :
        print("Nb de joueur modifié : ", self.gameType.get())

    def showIaLevel(self) :
        print("Niveau de lIA modifié : ", self.iaLevel.get())

    def draw(self) -> None :
        #Titre de la page :
        title = Label(self, anchor="nw", justify="center",text="Options",bg=self.bg, fg="white", font=("Roboto Bold", 50 * -1))
        title.place(x=519, y=48)

        #Elements graphiques pour le choix du type de jeux :
        typeLabel = Label(self, anchor="nw", justify="center",text="Type de jeu :",bg=self.bg, fg="white", font=("Roboto Medium", 34 * -1))
        typeLabel.place(x=274, y=147)
        oneP_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Un joueur", variable=self.gameType, value="1 joueur", command=lambda:self.updateConfig(), activebackground="#557CE0", bg=self.bg, fg="white", selectcolor="black", activeforeground="white", font=("Roboto Medium", 34 * -1))
        oneP_RadioButton.place(x=500, y=147)
        twoP_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Deux joueurs", variable=self.gameType, value="2 joueurs", command=lambda:self.updateConfig(), activebackground="#557CE0", bg=self.bg, fg="white",  selectcolor="black", activeforeground="white", font=("Roboto Medium", 34 * -1))
        twoP_RadioButton.place(x=850, y=147)

        #Elements graphiques pour le choix du niveau de l'IA :
        iaLabel = Label(self, anchor="nw", justify="center",text="Niveau de l'IA :",bg=self.bg, fg="white", font=("Roboto Medium", 34 * -1))
        iaLabel.place(x=244, y=256)
        oneP_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Simple", variable=self.iaLevel, value="simple", command=lambda:self.updateConfig(), activebackground="#557CE0", bg=self.bg, fg="white", selectcolor="black", activeforeground="white", font=("Roboto Medium", 34 * -1))
        oneP_RadioButton.place(x=500, y=256)
        twoP_RadioButton = Radiobutton(self, anchor="nw", cursor="hand2", text="Avancée", variable=self.iaLevel, value="avancee", command=lambda:self.updateConfig(), activebackground="#557CE0", bg=self.bg, fg="white",  selectcolor="black", activeforeground="white", font=("Roboto Medium", 34 * -1))
        twoP_RadioButton.place(x=850, y=256)

        #Bouton retour :
        ReturnMenu_image = PhotoImage(file=self.controller.relative_to_assets("ReturnMenu.png"))
        ReturnMenuButton = Button(self, cursor="hand2", image=ReturnMenu_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Menu"),relief="flat")
        ReturnMenuButton.image=ReturnMenu_image
        ReturnMenuButton.place(x=388.0,y=553.0,width=423.0,height=92.0)
        
