from tkinter import Button, Frame, PhotoImage, Label

class Options (Frame):
    def __init__(self, parent, controller, bg) -> None :
        #attributes :
        Frame.__init__(self, parent, bg=bg)
        
        self.assets_path = controller.assets_path

        #init :
        self.draw()

    def relative_to_assets(self, path: str) -> str:
            return self.assets_path+"/"+path

    def draw(self) -> None :
        label = Label(self, text="This is the option page")
        label.pack(side="top", fill="x", pady=50)
        
