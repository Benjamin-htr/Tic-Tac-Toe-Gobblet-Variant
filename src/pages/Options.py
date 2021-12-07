from tkinter import Button, Frame, PhotoImage, Label

class Options (Frame):
    def __init__(self, parent, controller, bg) -> None :
        Frame.__init__(self, parent, bg=bg)
        
        #attributes :
        self.bg = bg
        self.controller = controller
        
        #init :
        self.draw()



    def draw(self) -> None :
        title = Label(self, anchor="nw", justify="center",text="Options",bg=self.bg, fg="white", font=("Roboto Bold", 50 * -1))
        title.place(x=519, y=48)


        ReturnMenu_image = PhotoImage(file=self.controller.relative_to_assets("ReturnMenu.png"))
        ReturnMenuButton = Button(self, cursor="hand2", image=ReturnMenu_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Menu"),relief="flat")
        ReturnMenuButton.image=ReturnMenu_image
        ReturnMenuButton.place(x=388.0,y=553.0,width=423.0,height=92.0)
        
