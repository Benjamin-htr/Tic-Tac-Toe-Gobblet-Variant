from tkinter import Button, Frame, PhotoImage, Label
from tkinter.messagebox import askyesno


class Game (Frame):
    def __init__(self, parent, controller, bg) -> None :
        Frame.__init__(self, parent, bg=bg)
        

        #attributes :
        self.bg = bg
        self.controller = controller
        
        #init :
        self.drawPage()

    def drawPage(self) -> None :
        #Titre de la page :
        title = Label(self, anchor="nw", justify="center",text="Partie en cours",bg=self.bg, fg="white", font=("Roboto Bold", 40 * -1))
        title.place(x=437.0, y=16.0)

        self.drawGrid()

        QuitButton_image = PhotoImage(file=self.controller.relative_to_assets("QuitGame.png"))
        QuitButton = Button(self, cursor="hand2", image=QuitButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.quitGame(),relief="flat")
        QuitButton.image=QuitButton_image
        QuitButton.place(x=455.0,y=624.0,width=290.0,height=55.0)
        
    def drawGrid(self) -> None :
        EmptyCase_image = PhotoImage(file=self.controller.relative_to_assets("EmptyCase.png"))

        #Colonne 1 :
        L1C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L1C1 clicked"),relief="flat")
        L1C1.image=EmptyCase_image
        L1C1.place(x=140.0,y=195.0,width=105.0,height=105.0)

        L2C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L2C1 clicked"),relief="flat")
        L2C1.image=EmptyCase_image
        L2C1.place(x=140.0,y=317.0,width=105.0,height=105.0)

        L3C1 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L3C1 clicked"),relief="flat")
        L3C1.image=EmptyCase_image
        L3C1.place(x=140.0,y=439.0,width=105.0,height=105.0)

        #Colonne 2 :
        L1C2 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L1C2 clicked"),relief="flat")
        L1C2.image=EmptyCase_image
        L1C2.place(x=262.0,y=195.0,width=105.0,height=105.0)

        L2C2 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L2C2 clicked"),relief="flat")
        L2C2.image=EmptyCase_image
        L2C2.place(x=262.0,y=317.0,width=105.0,height=105.0)

        L3C2 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L3C2 clicked"),relief="flat")
        L3C2.image=EmptyCase_image
        L3C2.place(x=262.0,y=439.0,width=105.0,height=105.0)

        #Colonne 3 :
        L1C3 = Button(self, image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L1C3 clicked"),relief="flat")
        L1C3.image=EmptyCase_image
        L1C3.place(x=384.0,y=195.0,width=105.0,height=105.0)

        L2C3 = Button(self,  image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L2C3 clicked"),relief="flat")
        L2C3.image=EmptyCase_image
        L2C3.place(x=384.0,y=317.0,width=105.0,height=105.0)

        L3C3 = Button(self,  image=EmptyCase_image,cursor="hand2", borderwidth=0,highlightthickness=0,command=lambda: print("L3C3 clicked"),relief="flat")
        L3C3.image=EmptyCase_image
        L3C3.place(x=384.0,y=439.0,width=105.0,height=105.0)

        return None
    
    
    def quitGame(self) -> None :
        print('quitGame')
        answer = askyesno(title='Quitter', message='Etes vous sûr de vouloir quitter ?\nLa partie ne sera pas sauvegardée.')

        if answer :
            self.controller.show_frame("Menu")