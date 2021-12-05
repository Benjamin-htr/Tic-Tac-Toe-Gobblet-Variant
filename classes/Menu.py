from tkinter import Button, Frame, PhotoImage
from tkinter.messagebox import askyesno

class Menu (Frame):
    def __init__(self, parent, controller, bg) -> None :
        Frame.__init__(self, parent, bg=bg)

        #attributes :
        self.controller = controller
        
        #init :
        self.draw()

    def draw(self) -> None :
        NewGameButton_image = PhotoImage(file=self.controller.relative_to_assets("button_1.png"))
        NewGameButton = Button(self,image=NewGameButton_image,borderwidth=0,highlightthickness=0,command=lambda: print("button_1 clicked"),relief="flat")
        NewGameButton.image=NewGameButton_image
        NewGameButton.place( x=389.0, y=96.0, width=423.0, height=92.0)

        OptionsButton_image = PhotoImage(file=self.controller.relative_to_assets("button_2.png"))
        OptionsButton = Button(self,image=OptionsButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Options"),relief="flat")
        OptionsButton.image=OptionsButton_image
        OptionsButton.place(x=389.0,y=235.0,width=423.0,height=92.0)

        CreditsButton_image = PhotoImage(file=self.controller.relative_to_assets("button_3.png"))
        CreditsButton = Button(self,image=CreditsButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.controller.show_frame("Credits"),relief="flat")
        CreditsButton.image=CreditsButton_image
        CreditsButton.place(x=389.0,y=374.0,width=423.0,height=92.0)

        QuitButton_image = PhotoImage(file=self.controller.relative_to_assets("button_4.png"))
        QuitButton = Button(self,image=QuitButton_image,borderwidth=0,highlightthickness=0,command=lambda: self.quit(),relief="flat")
        QuitButton.image=QuitButton_image
        QuitButton.place(x=389.0,y=513.0,width=423.0,height=92.0)
        
    def quit(self) -> None :
        answer = askyesno(title='Quitter', message='Etes vous sûr de vouloir quitter ?')

        if answer :
            self.controller.quit()