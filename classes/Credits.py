from tkinter import Button, Frame, PhotoImage, Label

class Credits (Frame):
    def __init__(self, parent, controller, bg) -> None :
        Frame.__init__(self, parent, bg=bg)
        
        #attributes :
        self.controller = controller
        
        #init :
        self.draw()



    def draw(self) -> None :
        label = Label(self, text="This is the credits page")
        label.pack(side="top", fill="x", pady=50)
        
