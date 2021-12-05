from tkinter import Button, Frame, PhotoImage, Label
from tkinter import ttk

class Menu (Frame):
    def __init__(self, parent, controller, bg) -> None :
        Frame.__init__(self, parent, bg=bg)
        
        #attributes :
        self.controller = controller
        
        #init :
        self.draw()

    def draw(self) -> None :
        button_image_1 = PhotoImage(file=self.controller.relative_to_assets("button_1.png"))
        button_1 = Button(self,image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: print("button_1 clicked"),relief="flat")
        button_1.image=button_image_1
        button_1.place( x=389.0, y=96.0, width=423.0, height=92.0)

        button_image_2 = PhotoImage(file=self.controller.relative_to_assets("button_2.png"))
        button_2 = Button(self,image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda: print("button_2 clicked"),relief="flat")
        button_2.image=button_image_2
        button_2.place(x=389.0,y=235.0,width=423.0,height=92.0)

        button_image_3 = PhotoImage(file=self.controller.relative_to_assets("button_3.png"))
        button_3 = Button(self,image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: print("button_3 clicked"),relief="flat")
        button_3.image=button_image_3
        button_3.place(x=389.0,y=374.0,width=423.0,height=92.0)

        button_image_4 = PhotoImage(file=self.controller.relative_to_assets("button_4.png"))
        button_4 = Button(self,image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: print("button_4 clicked"),relief="flat")
        button_4.image=button_image_4
        button_4.place(x=389.0,y=513.0,width=423.0,height=92.0)
        
