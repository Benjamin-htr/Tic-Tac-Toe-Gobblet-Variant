from tkinter import Button, Frame, PhotoImage, Label

class Credits (Frame):
    def __init__(self, parent, controller, bg) -> None :
        Frame.__init__(self, parent, bg=bg)
        
        #attributes :
        self.bg = bg
        self.controller = controller
        
        #init :
        self.draw()



    def draw(self) -> None :
        title = Label(self, anchor="nw", justify="center",text="Crédits",bg=self.bg, fg="white", font=("Roboto Bold", 50 * -1))
        title.place(x=519, y=48)

        name = Label(self, anchor="nw",text="Developper : Hautier Benjamin", bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 30 * -1))
        name.place(x=382.0, y=144.0)

        versions = Label(self,anchor="nw", text="Python Version : 3.9.1\nExtern Libs : Tkinter (v8.6)",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 30 * -1))
        versions.place(x=382.0, y=229.0)

        git1 = Label(self,anchor="nw",text="Github Repo :",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 30 * -1)) 
        git1.place(x=344.0, y=367.0)
        git2 = Label(self,anchor="nw",text="https://github.com/Benjamin-htr/Tic-Tac-Toe-Gobblet-Variant",bg=self.bg, fg="#F2FADB",font=("Roboto Medium", 30 * -1)) 
        git2.place(x=344.0, y=405.0)

        ReturnMenu_image = PhotoImage(file=self.controller.relative_to_assets("ReturnMenu.png"))
        ReturnMenuButton = Button(self, cursor="hand2", image=ReturnMenu_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Menu"),relief="flat")
        ReturnMenuButton.image=ReturnMenu_image
        ReturnMenuButton.place(x=388.0,y=553.0,width=423.0,height=92.0)
